import pandas as pd
from sqlalchemy import create_engine,MetaData
from geoalchemy2 import Geometry
import matplotlib.pyplot as plt
import pycountry
import numpy as np
import requests

plt.style.use('ggplot')

class LandslideIncidentiPrecipitazione(object):

    def __init__(self, iso):

        self.ISO = iso
        self.IP_IN = "localhost"

        # DATI DA EM-DAT
        self.LANDSLIDES_EMDAT = "Landslide_" + str(self.ISO)
        self.SCHEMA_EMDAT = "em_dat"

        # DATI NASA
        self.LANDSLIDES_GLC = "glc_attribs"
        self.LANDSLIDES_GLC_SPARC = "glc20160114_wfp"
        self.SCHEMA_NASA = "nasa"
        self.RAIN_TRMM = 'trmm_' + str(self.ISO).lower() + '_0115'

        # DATI FAO
        self.PRECIPITATION_FAO_CHIRPS = 'sparc_month_prec'
        self.SCHEMA_PUBBLICO = "public"

        # DATI CONNESSION DB
        self.ENGINE_IN = create_engine(
            r'postgresql://geonode:geonode@' +
            self.IP_IN + '/geonode-imports')
        self.CONN_IN = self.ENGINE_IN.connect()
        self.oggetto_paese = pycountry.countries.get(alpha3=self.ISO)
        self.paese_nome = self.oggetto_paese.name

    def precipitazioneWorldBank(self):

        r_1980_1999 = requests.get(
            'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/pr/1980/1999/' + self.ISO)

        lista_valori_mensili_pioggia = []

        if r_1980_1999.status_code == 200:
            risposta = r_1980_1999.json()
            for valore_mensile in risposta[0]['monthVals']:
                lista_valori_mensili_pioggia.append(valore_mensile)
        else:
            print "Connection failed"

        return lista_valori_mensili_pioggia
        
    def nasaEvents(self):

        try:
            metadata_in = MetaData(
                self.CONN_IN,
                schema=self.SCHEMA_NASA)
        except Exception as e:
            print e.message

        df_glc = pd.read_sql_table(self.LANDSLIDES_GLC,self.ENGINE_IN,schema=metadata_in.schema,
                                   index_col='adm2_code',parse_dates=['date'])

        df_glc['mese'] = pd.to_datetime(df_glc['date']).dt.month
        df_glc['day'] = pd.to_datetime(df_glc['date']).dt.day
        df_glc['year'] = pd.to_datetime(df_glc['date']).dt.year
        df_glc['mese_testo'] = pd.to_datetime(df_glc['date']).dt.strftime("%b")
        df_glc['mese_testo'] = df_glc['mese_testo'].apply(lambda x: str(x).lower())

        return df_glc

    def emdatEvents(self):

        try:
            metadata_in = MetaData(self.CONN_IN, schema=self.SCHEMA_EMDAT)
        except Exception as e:
            print e.message

        df_emdat = pd.read_sql_table(
            self.LANDSLIDES_EMDAT,
            self.ENGINE_IN,
            schema=metadata_in.schema,
            index_col='index')

        if len(df_emdat) > 0:

            df_emdat['mese_fine'] = df_emdat['end_date'].str.split('/').str.get(1)
            df_emdat['mese_fine'].replace('', 0, inplace=True)
            df_emdat['mese_fine_int'] = df_emdat['mese_fine'].astype(np.int64)

            df_emdat['mese_inizio'] = df_emdat.start_date.str.split("/").str.get(1)
            df_emdat['mese_inizio'].replace('', 0, inplace=True)
            df_emdat['mese_inizio_int'] = df_emdat['mese_inizio'].astype(np.int64)

            conteggio = df_emdat['mese_inizio_int'].value_counts()
            conteggio = conteggio.sort_index()
            tabella_solo_landslides = df_emdat.loc[df_emdat['dis_subtype'] == 'Landslide']
            conteggio_solo_landslides = tabella_solo_landslides['mese_inizio_int'].value_counts()
            conteggio_solo_landslides = conteggio_solo_landslides.sort_index()

        else:
            pass

        conteggio_dict = dict(conteggio_solo_landslides)
        for mese in range(1, 13):
            if mese in conteggio_dict.iterkeys():
                pass
            else:
                conteggio_dict[mese] = 0

        conteggio_dict.pop('', None)
        conteggio_dict.pop(0, None)

        return df_emdat, conteggio_dict

class LandslideIncidentiPrecipitazioneAdmin2(LandslideIncidentiPrecipitazione):

    def __init__(self, iso_sub):
        super(LandslideIncidentiPrecipitazioneAdmin2,self).__init__(iso_sub)
    
    def faoPrecipitation(self):

        try:
            metadata_in = MetaData(self.CONN_IN, schema=self.SCHEMA_PUBBLICO)
        except Exception as e:
            print e.message

        df_precipitation_country_level = pd.read_sql_table(
            self.PRECIPITATION_FAO_CHIRPS,
            self.ENGINE_IN,
            schema=metadata_in.schema,
            index_col='adm2_code')

        df_precipitation_country_level.index = df_precipitation_country_level.index.str.rstrip()

        return df_precipitation_country_level

    def selezioneDatiFaoNasaSingolaAdm2(self, df_precipitation_country_fao, df_landslides_country_nasa, adm2_code):

        eventi_gcl_adm2 = pd.DataFrame()

        if len(df_precipitation_country_fao) > 0:
            pioggia_fao_adm2 = df_precipitation_country_fao.loc[adm2_code]
        else:
            pioggia_fao_adm2 = pd.DataFrame()

        if len(df_landslides_country_nasa) > 0:
            try:
                eventi_gcl_adm2 = df_landslides_country_nasa.loc[int(adm2_code)]
            except:
                eventi_gcl_adm2 = pd.DataFrame()

        return pioggia_fao_adm2, eventi_gcl_adm2

    def preparazioneDFDatiFAONASASingolaAdm(self,rains_pass,glcs_pass,area_adm_code):

        try:
            if glcs_pass.empty:
                print "No Landslides in %s " % area_adm_code
                print
                solo_valori_pioggia = rains_pass[6:]
                mesi_numerici = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                eventi_gcl_adm2 = pd.DataFrame(
                    {'mese_testo': [
                        'jan', 'feb', 'mar',
                        'apr', 'may', 'jun',
                        'jul', 'aug', 'sep',
                        'oct', 'nov', 'dec'],
                     'eventi': np.array([0.00] * 12, dtype='float16')
                     })
                eventi_gcl_adm2 = eventi_gcl_adm2.set_index('mese_testo')
            else:
                solo_valori_pioggia = rains_pass[6:]
                glcs_pass = glcs_pass.dropna()
                if isinstance(glcs_pass, pd.DataFrame):
                    mesi_numerici = [4, 8, 12, 2, 1, 7, 6, 3, 5, 11, 10, 9]
                    try:
                        casi_mensili = glcs_pass.groupby('mese_testo').count()
                        eventi_gcl_adm2 = casi_mensili.iloc[:, :1]
                    except Exception, e:
                        print str(e)
                        pass
                elif isinstance(glcs_pass, pd.Series):
                    # serie
                    mesi_numerici = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    try:
                        print glcs_pass.mese
                        il_mese_registrato = int(glcs_pass.mese)
                        print "ci sarebbe %d" % il_mese_registrato
                        eventi_gcl_adm2 = pd.DataFrame(
                            {'mese_testo': ['jan', 'feb', 'mar',
                                            'apr', 'may', 'jun',
                                            'jul', 'aug', 'sep',
                                            'oct', 'nov', 'dec'],
                                'eventi': np.array([0.00] * 12, dtype='float16')
                            })
                        eventi_gcl_adm2 = eventi_gcl_adm2.set_index('mese_testo')
                        eventi_gcl_adm2['eventi'][il_mese_registrato-1] = 1
                    except Exception as inst:
                        eventi_gcl_adm2 = pd.DataFrame(
                            {'mese_testo': ['jan', 'feb', 'mar',
                                            'apr', 'may', 'jun',
                                            'jul', 'aug', 'sep',
                                            'oct', 'nov','dec'],
                                 'eventi': np.array([0.00] * 12, dtype='float16')
                             })
                        eventi_gcl_adm2 = eventi_gcl_adm2.set_index('mese_testo')
        except Exception as inst:
            print inst

        return solo_valori_pioggia, eventi_gcl_adm2, mesi_numerici

    def correlazioneDFNasaFaoNormalizzazione(self,solo_valori_pioggia_pass, eventi_gcl_adm_pass,mesi_numerici_pass):

        # print eventi_gcl_adm_pass
        dati_correlati = pd.concat([solo_valori_pioggia_pass, eventi_gcl_adm_pass], axis=1)

        dati_correlati.columns = ['mm', 'eventi']
        dati_correlati['mm_norm'] = (dati_correlati['mm'] - dati_correlati['mm'].min()) / \
                                    (dati_correlati['mm'].max() - dati_correlati['mm'].min())
        dati_correlati['eventi'].fillna(0, inplace=True)
        dati_correlati['eventi_norm'] = (dati_correlati['eventi'] - dati_correlati['eventi'].min()) / (
                                         dati_correlati['eventi'].max() - dati_correlati['eventi'].min())
        dati_correlati['eventi_norm'].fillna(0, inplace=True)


        dati_correlati.index = mesi_numerici_pass
        dati_correlati = dati_correlati.sort_index(axis=0)
        dati_normalizzati = dati_correlati.loc[1:, 'mm_norm':'eventi_norm']

        return dati_normalizzati

    def plotCorrelatedDataNasaFao(self, adm_name, associazione_pioggia_frane_normalizzata):

        associazione_pioggia_frane_normalizzata['mm_norm'].plot(
            label='CHIRPS/FAO',
            color='red')

        associazione_pioggia_frane_normalizzata['eventi_norm'].plot(
            label='NASA',
            kind="bar",
            color='green')

        plt.legend()
        plt.title(adm_name)
        plt.show()

class LandslideIncidentiPrecipitazioneNazionale(LandslideIncidentiPrecipitazione):

    def __init__(self, iso_sub):
        super(LandslideIncidentiPrecipitazioneNazionale, self).__init__(iso_sub)

    def trmmPrecipitationByCountry(self):

        try:
            metadata_in = MetaData(self.CONN_IN, schema=self.SCHEMA_NASA)
        except Exception as e:
            print e.message

        df_prec_trmm = pd.read_sql_table(
            self.RAIN_TRMM,
            self.ENGINE_IN,
            schema=metadata_in.schema,
            index_col='row.names')
        df_prec_trmm['mm_day'] = df_prec_trmm['in_day'] * 25.4

        return df_prec_trmm

    def national_assessment(self, glcs_country, rains_trmm):

        glcs_country_grp = glcs_country.groupby("mese")["iso3"].count()

        rains_trmm['data_mis'] = rains_trmm['data_mis'].astype('datetime64[ns]')
        rains_trmm = rains_trmm.set_index('data_mis')
        rains_trmm['day'] = rains_trmm.index.day
        rains_trmm['mese'] = rains_trmm.index.month
        rains_trmm['year'] = rains_trmm.index.year

        media_storica_mensile = rains_trmm.groupby("mese")["in_day", "mm_day"].mean()
        media_storica_mensile['mese'] = media_storica_mensile.index
        media_storica_mensile.columns = ["avg_inches", "avg_mm", "mese"]

        rains_trmm = pd.merge(rains_trmm,
                              media_storica_mensile,
                              on='mese',
                              how='inner')
        rains_trmm['above'] = rains_trmm['mm_day'] > rains_trmm['avg_mm']

        rains_trmm_solo_sopra = rains_trmm[rains_trmm['above'] == True].copy()
        rains_trmm_solo_sopra['data'] = pd.to_datetime(rains_trmm_solo_sopra.year * 10000 + rains_trmm_solo_sopra.mese * 100 + rains_trmm_solo_sopra.day,format='%Y%m%d')
        rains_trmm_solo_sopra['delta'] = rains_trmm_solo_sopra['data'].diff()

        mask_3 = (rains_trmm_solo_sopra['delta'] > '1 days') &\
                 (rains_trmm_solo_sopra['delta'] <= '3 days')
        mesi_sopra_3gg = rains_trmm_solo_sopra[mask_3]
        mesi_sopra_3gg_grp = mesi_sopra_3gg.groupby("mese")["above"].sum()

        mask_5 = (rains_trmm_solo_sopra['delta'] > '3 days') &\
                 (rains_trmm_solo_sopra['delta'] <= '5 days')
        mesi_sopra_5gg = rains_trmm_solo_sopra[mask_5]
        mesi_sopra_5gg_grp = mesi_sopra_5gg.groupby("mese")["above"].sum()

        mask_15 = (rains_trmm_solo_sopra['delta'] > '5 days') & (rains_trmm_solo_sopra['delta'] <= '15 days')
        mesi_sopra_15gg = rains_trmm_solo_sopra[mask_15]
        mesi_sopra_15gg_grp = mesi_sopra_15gg.groupby("mese")["above"].sum()

        df_rain_events = pd.DataFrame(dict(d3=mesi_sopra_3gg_grp,
                                           d5=mesi_sopra_5gg_grp,
                                           d15=mesi_sopra_15gg_grp,
                                           ev=glcs_country_grp)).reset_index()

        df_rain_events['adm0_code'] = self.ISO
        df_rain_events['adm0_name'] = self.paese_nome
        df_rain_events['d3_n'] = (df_rain_events['d3'] - df_rain_events['d3'].min()) /\
                                 (df_rain_events['d3'].max() - df_rain_events['d3'].min())
        df_rain_events['d5_n'] = (df_rain_events['d5'] - df_rain_events['d5'].min()) /\
                                 (df_rain_events['d5'].max() -  df_rain_events['d5'].min())
        df_rain_events['d15_n'] = (df_rain_events['d15'] - df_rain_events['d15'].min()) /\
                                  (df_rain_events['d15'].max() - df_rain_events['d15'].min())
        df_rain_events['ev_n'] = (df_rain_events['ev'] - df_rain_events['ev'].min()) /\
                                 (df_rain_events['ev'].max() - df_rain_events['ev'].min())

        df_rain_events['d3_n'].plot(label='3 days', color='red')
        df_rain_events['d5_n'].plot(label='5 days', color='orange')
#         df_rain_events['d15_n'].plot(label='15 days', color='darkmagenta')
        df_rain_events['ev_n'].plot(label='Events', kind="bar", color='green')

        plt.legend()
        plt.title(self.paese_nome)
        plt.show()

        return df_rain_events

    def data_fetching(self):

        engine_in = create_engine(r'postgresql://geonode:geonode@' + self.IP_IN + '/geonode-imports')

        try:
            df_in_sql = pd.read_sql_table(self.LANDSLIDES_GLC_SPARC, engine_in, schema=self.SCHEMA_NASA, index_col='id', parse_dates={'date': '%Y-%m-%d'})
        except Exception as e:
            print e.message

        return df_in_sql

    def data_cleaning(self,df):

        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year
        tabella_lavoro = df[df['iso3'] == self.ISO]

        return tabella_lavoro

    def data_analysis_vizualization(self,tabella_aggiustata):
           
        incidenti_per_meseSerie = tabella_aggiustata.groupby(['rcl_type','month'])['month'].count()
        incidenti_per_meseDataFrame = tabella_aggiustata.groupby(['rcl_type','month']).count()
        
        solo_landslides = incidenti_per_meseDataFrame.loc['Landslide','iso3']
          
        plt.plot(solo_landslides)
        plt.title('NASA Registered Landslides')
        plt.show()
