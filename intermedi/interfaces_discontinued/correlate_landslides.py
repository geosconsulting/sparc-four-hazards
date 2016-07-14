__author__ = 'fabio.lana'

import pandas as pd
from sqlalchemy import create_engine, MetaData
import matplotlib.pyplot as plt
import requests
# from pandas.io import wb
import pycountry
import numpy as np
import csv
from bs4 import BeautifulSoup


from intermedi.utilita import all_plots

def richieste_wordlBank(iso3_paese):

    monthly_avg_1980_1999 = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/pr/1980/1999/' + iso3_paese)
    # monthly_anom_1980_1999 = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/pr/1980/1999/' + iso3_paese)
    # temperature_avg_1980_1999 = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/' + iso3_paese)

    lista_valori_mensili_pioggia = []
    dct_valori_mensili_pioggia = {}

    contatore = 1
    if monthly_avg_1980_1999.status_code == 200:
        risposta = monthly_avg_1980_1999.json()
        print risposta[0]
        # for valore_mensile in risposta[0]['monthVals']:
        #     lista_valori_mensili_pioggia.append(valore_mensile)
        #     dct_valori_mensili_pioggia[contatore] = valore_mensile
        #     contatore += 1
    else:
        print "Connection failed"

    return lista_valori_mensili_pioggia, dct_valori_mensili_pioggia #, monthly_anom_1980_1999, temperature_avg_1980_1999

def emdat_events(ip_in, table_name):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')
    
    try:
        conn_in = engine_in.connect()
        metadata_in = MetaData(conn_in, schema="em_dat")
    except Exception as e:
        print e.message

    df_in_sql = pd.read_sql_table(table_name, engine_in, schema=metadata_in.schema, index_col='index')

    return df_in_sql

def fao_prec_events(ip_in, table_name_rain):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')

    try:
        conn_in = engine_in.connect()
        metadata_in = MetaData(conn_in, schema="public")
    except Exception as e:
        print e.message

    df_in_sql = pd.read_sql_table(table_name_rain, engine_in, schema=metadata_in.schema, index_col='adm2_code')
    df_in_sql.index = df_in_sql.index.str.rstrip()

    return df_in_sql

def fao_servizio_coordinata(lat,lon):

    stringola = "http://geonetwork3.fao.org/aglw/climate6x.php?xcoord=" + lat +"&ycoord=" + lon +"&dddms=dd"
    tutti_frutti = requests.get(stringola)

    soup = BeautifulSoup(tutti_frutti.text,"lxml")
    table = soup.find("table", attrs={"class": "queryResults"})
    # tb_df = pd.read_html(stringola)
    # print table

    # The first tr contains the field names.
    headings = [tr.get_text() for tr in table.find("tr").find_all("td")]
    headings[1] = 'Prc. Month'
    headings[2] = 'Prc. Day'
    headings[12] = 'Eto. Month'
    headings[13] = 'Eto. Day'

    datasets = []
    for row in table.find_all("tr")[2:14]:
        # dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
        dataset = [td.get_text() for td in row.find_all("td")]
        datasets.append(dataset)

    df_valori = pd.DataFrame(datasets, columns=headings)
    df_valori = df_valori.set_index('Month')
    # df_valori[2] = df_valori['Prc.Day']
    # print df_valori.describe()
    # print df_valori.dtypes

    # serie_prec = df_valori['Prc. Month']
    # print type(serie_prec)
    return df_valori

def scelta_equazione(ip_in,table_thresholds):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')

    try:
        conn_in = engine_in.connect()
        metadata_in = MetaData(conn_in, schema="public")
    except Exception as e:
        print e.message

    df_thresholds = pd.read_sql_table(table_thresholds, engine_in, schema=metadata_in.schema, index_col='id')

    return df_thresholds

def data_analysis():

    # scelta_equazione()
    valori_ritornati = fao_servizio_coordinata("34.83", "31.17")
    # print valori_ritornati
    mesi = list(valori_ritornati.index)
    pioggia = list(valori_ritornati['Prc. Month'])

    # plt.plot(pioggia, mesi)
    # plt.show()

    ip_in = 'localhost'
    iso = 'COL'
    oggetto_paese = pycountry.countries.get(alpha3=iso)
    paese_nome = oggetto_paese.name

    # indicators = ['NY.GDP.PCAP.KD', 'SP.POP.TOTL', 'SP.POP.0014.TO.ZS', 'SP.POP.65UP.TO.ZS', 'AG.LND.AGRI.ZS',
    #               'AG.YLD.CREL.KG', 'SP.RUR.TOTL', 'SH.STA.MALN.ZS', 'GC.BAL.CASH.GD.ZS', 'NE.EXP.GNFS.ZS',
    #               'NE.IMP.GNFS.ZS']
    #
    # iso2 = oggetto_paese.alpha2
    # dati_nazionali = wb.download(indicator=indicators, country=[iso2], start=2006, end=2014)
    # dati_nazionali.columns = ['GDP Per Capita','Total Pop', 'Pop Age 0-14', 'Pop Age 65-up',
    #              'Perc Agr Land','Cereal Yeld', 'Rural Population', 'Malnutrition Age<5',
    #              'Cash Surplus-Deficit','Export', 'Import', ]
    # print dati_nazionali

    # dati_nazionali['Total Pop'].plot(kind='bar',)
    # plt.show()

    # print dati_nazionali['GDP Per Capita'].groupby(level=0).mean()

    # dati_nazionali['Importer'] = dati_nazionali['Export'] - dati_nazionali['Import']
    # print dati_nazionali

    # sub_indicators = ['SI.POV.NAHC','SI.POV.RUHC', 'SI.POV.URHC']
    # dati_sub_national = wb.download(indicator=indicators, country=[iso2], start=2006, end=2014)
    # print dati_sub_national
    # dati_sub_national.plot(kind='bar')
    # plt.show()

    table_name = 'Landslide_' + iso
    # table_name = 'central_africa'
    tabella = emdat_events(ip_in, table_name)
    # print tabella
    if len(tabella) > 0:
        tabella['mese_fine'] = tabella['end_date'].str.split('/').str.get(1)
        tabella['mese_fine'].replace('', 0, inplace=True)
        tabella['mese_fine_int'] = tabella['mese_fine'].astype(np.int64)

        tabella['mese_inizio'] = tabella.start_date.str.split("/").str.get(1)
        tabella['mese_inizio'].replace('', 0, inplace=True)
        tabella['mese_inizio_int'] = tabella['mese_inizio'].astype(np.int64)

        conteggio = tabella['mese_inizio_int'].value_counts()
        conteggio = conteggio.sort_index()
        # print conteggio
        # conteggio.plot(kind='bar')
        # plt.title(paese_nome)
        # plt.show()
        tabella_solo_landslides = tabella.loc[tabella['dis_subtype'] == 'Landslide']
        conteggio_solo_landslides = tabella_solo_landslides['mese_inizio_int'].value_counts()
        conteggio_solo_landslides = conteggio_solo_landslides.sort_index()
        # print conteggio_solo_landslides, type(conteggio_solo_landslides)
        # print conteggio_solo_landslides.index
        # conteggio_solo_landslides.plot(kind='bar')
        # plt.title(paese_nome)
        # plt.show()
        # tabella.to_csv(table_name + ".csv")
    else:
        pass

    conteggio_dict = dict(conteggio)
    for mese in range(1, 13):
        if mese in conteggio_dict.iterkeys():
            pass
        else:
            conteggio_dict[mese] = 0

    conteggio_dict.pop('', None)
    conteggio_dict.pop(0, None)

    print conteggio_dict
    plt.grid(True)

    # Plot y1 vs x in blue on the left vertical axis.
    plt.xlabel("Months")
    plt.ylabel("Historical Incidents related with LANDSLIDES EM-DAT", color="b")
    plt.tick_params(axis="y", labelcolor="b")
    plt.bar(range(len(conteggio_dict)), conteggio_dict.values(), align='center', color='g', label='Incidents')
    plt.xticks(range(len(conteggio_dict)), conteggio_dict.keys())

    # plt.twinx()
    # plt.ylabel(labella_y, color="r")
    # plt.tick_params(axis="y", labelcolor="r")
    # plt.plot(range(len(list_ordered)), list_ordered.values(), 'r--')
    # plt.xticks(range(len(list_ordered)), list_ordered.keys())

    plt.title(table_name)
    plt.legend()
    plt.show()

    table_rain_name = 'sparc_month_prec'
    tabella_rain = fao_prec_events(ip_in, table_rain_name)

    # if len(tabella_rain) > 0:
    #     # print tabella_rain.head()
    #     pioggia_adms2 = tabella_rain.loc[:, 'jan':]
    #     # print pioggia_adms2.head()
    #     # print pioggia_adms2.ix[3519]
    #     # print pioggia_adms2.info()
    #     # print pioggia_adms2.describe()
    #     vuzzulo = pioggia_adms2.loc['40822']
    # else:
    #     pass
    #
    # valori_precipitazione_bancaMondiale_nazionale = precipitazioneWorldBank(ISO)
    # print valori_precipitazione_bancaMondiale_nazionale[1]
    #
    # # ivaloraggi = all_plots.plot_monthly_mean_wb(ISO, valori_precipitazione_bancaMondiale_nazionale[0], "World Bank Historical Precipitation")
    # ivaloraggi1 = all_plots.plot_monthly_mean_wb(ISO, vuzzulo, "FAO Historical Precipitation")

    # dict_finale = all_plots.historical_analysis_damages(paese_nome)
    # labella_y = "Precipitation (mm) Real Time World Bank"
    # all_plots.plot_monthly_danni("EM-DAT Registered Incidents", labella_y, ISO, ivaloraggi, dict_finale)

    # table_thresholds = 'sparc_landslides_thresholds'
    # table_thresholds = scelta_equazione(IP_IN, table_thresholds)
    # if len(table_thresholds) > 0:
    #     print table_thresholds
    # else:
    #     pass

if __name__ == "__main__":
    data_analysis()
