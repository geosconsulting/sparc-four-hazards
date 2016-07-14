# -*- coding: utf-8 -*-

import CompleteProcessingDrought as completeDrought
import CompleteProcessingLandslide as completeLandslide
# import Correlation_GLCFAO
import CorrelazioneIncidentiPrecipitazioneLandslide as CIP
import FloodDataManualUpload as fdup
from intermedi.interfaces_discontinued import glc_splitMese

from Tkinter import *
import tkMessageBox
import ttk
import pycountry

import psycopg2
from psycopg2.extensions import AsIs


class AppSPARC:
    def __init__(self, finestra):

        self.dbname = "geonode-imports"
        self.user = "geonode"
        self.password = "geonode"
        self.lista_amministrazioni = None

        finestra.geometry("450x340+30+30")

        self.area_messaggi = Text(finestra,
                                  background="black",
                                  foreground="green")

        self.area_messaggi.place(x=18, y=30, width=282, height=305)

        self.scr = Scrollbar(finestra, command=self.area_messaggi.yview)
        self.scr.place(x=8, y=30, width=10, height=275)
        self.area_messaggi.config(yscrollcommand=self.scr.set)

        self.collect_codes_country_level()
        self.box_value_adm0 = StringVar()
        self.box_adm0 = ttk.Combobox(finestra,
                                     textvariable=self.box_value_adm0)
        self.box_adm0['values'] = self.lista_paesi
        self.box_adm0.current(0)
        self.box_adm0.place(x=25, y=2, width=210, height=25)

        # SECTION FOR FLOOD CALCULATION
        # SECTION FOR FLOOD CALCULATION
        frame_flood = Frame(finestra, height=32, width=400, bg="blue")
        frame_flood.place(x=305, y=30, width=140, height=70)

        self.button_flood = Button(finestra,
                                   text="Flood Assessment",
                                   fg="blue")
        self.button_flood.bind('<Button-1>',
                               lambda scelta: scegli_calcolo("flood"))
        self.button_flood.place(x=310, y=35, width=130, height=25)

        self.button_flood_upload = Button(finestra,
                                          text="Upload Data Manually",
                                          fg="blue",
                                          command=self.flood_upload)
        self.button_flood_upload.place(x=310, y=70, width=130, height=25)
        # SECTION FOR FLOOD CALCULATION
        # SECTION FOR FLOOD CALCULATION

        # SECTION FOR DROUGHT CALCULATION
        # SECTION FOR DROUGHT CALCULATION
        frame_drought = Frame(finestra, height=80, width=400, bg="maroon")
        frame_drought.place(x=305, y=105, width=140, height=70)

        self.button_drought = Button(finestra,
                                     text="Drought Assessment",
                                     fg="maroon")
        self.button_drought.place(x=310, y=110, width=130, height=25)
        self.button_drought.bind('<Button-1>',
                                  lambda scelta: scegli_calcolo("drought"))

        self.button_drought_upload = Button(finestra,
                                            text="Upload Data Manually",
                                            fg="maroon",
                                            command=self.drought_upload)
        self.button_drought_upload.place(x=310, y=145, width=130, height=25)
        # SECTION FOR DROUGHT CALCULATION
        # SECTION FOR DROUGHT CALCULATION

        # SECTION FOR LANDSLIDES CALCULATION
        # SECTION FOR LANDSLIDES CALCULATION
        frame_landslide = Frame(finestra, height=260, width=400, bg="orange")
        frame_landslide.place(x=305, y=180, width=140, height=155)

        self.button_landslide = Button(finestra,
                                       text="Landslide Assessment",
                                       fg="black")
        self.button_landslide.place(x=310, y=185, width=130, height=25)
        self.button_landslide.bind('<Button-1>',
                                    lambda scelta: scegli_calcolo("landslide"))

        self.button_landslide_upload = Button(finestra,
                                              text="Upload Data Manually",
                                              fg="black",
                                              command=self.landslide_iso_cleaning)
        self.button_landslide_upload.place(x=310, y=215, width=130, height=25)

        self.button_landslide_upload = Button(finestra,
                                              text="Monthly Adm2",
                                              fg="black",
                                              command=self.landslide_adm2)
        self.button_landslide_upload.place(x=310, y=245, width=130, height=25)

        self.button_landslide_upload = Button(finestra,
                                              text="National Assessment",
                                              fg="black",
                                              command=self.landslide_adm0)
        self.button_landslide_upload.place(x=310, y=275, width=130, height=25)

        self.button_landslide_upload = Button(finestra,
                                              text="NASA/WB by month",
                                              fg="black",
                                              command=self.landslide_mensile_NASA_WB_nazionale)

        self.button_landslide_upload.place(x=310, y=305, width=130, height=25)
        # SECTION FOR LANDSLIDES CALCULATION
        # SECTION FOR LANDSLIDES CALCULATION

        def scegli_calcolo(scelta):

            attivo_nonAttivo = self.var_check.get()
            paese = self.box_value_adm0.get()

            if attivo_nonAttivo == 0 and scelta == 'flood':
                self.national_calc_flood(paese)
            elif attivo_nonAttivo == 1 and scelta == 'flood':
                verifica = tkMessageBox.askyesno("Warning",
                                                 "Ci vediamo domani...!!" +
                                                 "Continuo?")
                if verifica:
                    self.world_calc_flood()
                else:
                    pass

            if attivo_nonAttivo == 0 and scelta == 'drought':
                self.national_calc_drought(paese)
            elif attivo_nonAttivo == 1 and scelta == 'drought':
                verifica = tkMessageBox.askyesno("Warning",
                                                 "Ci vediamo domani...!!" +
                                                 "Continuo?")
                if verifica:
                                    self.world_calc_drought()
                else:
                    pass

            if attivo_nonAttivo == 0 and scelta == 'landslide':
                self.national_calc_landslide(paese)
            elif attivo_nonAttivo == 1 and scelta == 'landslide':
                verifica = tkMessageBox.askyesno("Warning",
                                                 "Non implementato!")
                pass
                # if verifica == True:
                #     pass
                # else:
                #     pass

        def attiva_disattiva():

            attivo_nonAttivo = self.var_check.get()
            if attivo_nonAttivo == 0:
                self.box_adm0.config(state='normal')
                self.button_flood_upload.config(state='normal')
                self.button_drought_upload.config(state='normal')
            else:
                self.box_adm0.config(state='disabled')
                self.button_flood_upload.config(state='disabled')
                self.button_drought_upload.config(state='disabled')

        self.var_check = IntVar()
        self.check_all = Checkbutton(finestra,
                                     text="All Countries",
                                     variable=self.var_check,
                                     command=attiva_disattiva)
        self.check_all.place(x=310, y=5, width=120, height=25)

        finestra.mainloop()

    def collect_codes_country_level(self):

        paesi = completeDrought.ManagePostgresDBDrought(self.dbname, self.user, self.password)
        self.lista_paesi = paesi.all_country_db()

    def national_calc_drought(self, paese):

        db_conn_drought = completeDrought.ManagePostgresDBDrought(self.dbname,
                                                                  self.user,
                                                                  self.password)
        lista_admin2 = db_conn_drought.admin_2nd_level_list(paese)

        for amministrazione in lista_admin2[1].iteritems():
            code_admin = amministrazione[0]
            nome_admin = amministrazione[1]['name_clean']

            db_conn_drought.file_structure_creation(nome_admin, code_admin)
            newDroughtAssessment = completeDrought.HazardAssessmentDrought(self.dbname,
                                                                           self.user,
                                                                           self.password)
            newDroughtAssessment.extract_poly2_admin(paese,
                                                     nome_admin,
                                                     code_admin)

            section_pop_raster_cut = newDroughtAssessment.cut_rasters_drought(paese,
                                                                              nome_admin,
                                                                              code_admin)

            if section_pop_raster_cut == "sipop":
                self.area_messaggi.insert(INSERT, "Population clipped....")
            elif section_pop_raster_cut == "nopop":
                self.area_messaggi.insert(INSERT, 
                    "Population raster not available....")
                sys.exit()

        dizio_drought = db_conn_drought.collect_drought_population_frequencies_frm_dbfs()
        self.area_messaggi.insert(INSERT, "Data Collected\n")
        adms = set()
        for chiave, valori in sorted(dizio_drought.iteritems()):
            adms.add(chiave.split("-")[1])
        insert_list = db_conn_drought.prepare_insert_statements_drought_monthly_values(adms, dizio_drought)[2]
        self.area_messaggi.insert(INSERT, "Data Ready for Upload in DB\n")

        if db_conn_drought.check_if_monthly_table_drought_exists() == '42P01':
            db_conn_drought.create_sparc_drought_population_month()
            db_conn_drought.insert_drought_in_postgresql(insert_list)

        if db_conn_drought.check_if_monthly_table_drought_exists() == 'exists':
            self.area_messaggi.insert(INSERT, "Table Drought Exist\n")
            db_conn_drought.clean_old_values_month_drought(paese)
            db_conn_drought.save_changes()
            db_conn_drought.insert_drought_in_postgresql(insert_list)

        db_conn_drought.save_changes()
        db_conn_drought.close_connection()
        self.area_messaggi.insert(INSERT, "Data for " + paese + " Uploaded in database\n")

    def world_calc_drought(self):

        paesi = self.lista_paesi
        for paese in paesi:
            self.national_calc_drought(paese)

    def drought_upload(self):

        paese = self.box_value_adm0.get()

        import DroughtDataManualUpload as ddup

        proj_dir = "c:/data/tools/sparc/projects/drought/"
        dirOutPaese = proj_dir + paese

        raccogli_da_files_anno = ddup.collect_drought_poplation_frequencies_frm_dbfs(dirOutPaese)
        adms = set()
        for chiave, valori in sorted(raccogli_da_files_anno.iteritems()):
            adms.add(chiave.split("-")[1])
        raccolti_anno = ddup.prepare_insert_statements_drought_monthly_values(paese, adms, raccogli_da_files_anno)
        risultato = ddup.insert_drought_in_postgresql(paese, raccolti_anno[2])
        self.area_messaggi.insert(INSERT, risultato)

    def national_calc_flood(self, paese):

        import CountryCalculationsFlood

        calcolo = CountryCalculationsFlood.data_processing_module_flood(paese)
        self.area_messaggi.insert(INSERT, calcolo)

        data_upload = CountryCalculationsFlood.data_upload_module_flood(paese)
        self.area_messaggi.insert(INSERT, data_upload)

    def world_calc_flood(self):

        paesi = self.lista_paesi
        for paese in paesi:
            self.national_calc_flood(paese)

    def flood_upload(self):

        paese = self.box_value_adm0.get()

        proj_dir = "c:/data/tools/sparc/projects/floods/"
        dirOutPaese = proj_dir + paese
        fillolo = dirOutPaese + "/" + paese + ".txt"

        raccogli_da_files_anno = fdup.collect_annual_data_byRP_from_dbf_country(dirOutPaese)
        adms = []
        for raccolto in raccogli_da_files_anno:
            adms.append(raccolto)
        raccolti_anno = fdup.process_dict_with_annual_values(paese,
                                                             adms,
                                                             raccogli_da_files_anno,
                                                             fillolo)
        fdup.inserisci_postgresql(paese, raccolti_anno[2])
        raccolti_mese = fdup.raccogli_mensili(fillolo)
        risultato = fdup.inserisci_postgresql(paese, raccolti_mese)
        self.area_messaggi.insert(INSERT, risultato)

    def national_calc_landslide(self, paese):

        db_conn_landslide = completeLandslide.ManagePostgresDBLandslide(self.dbname, self.user, self.password)
        lista_admin2 = db_conn_landslide.admin_2nd_level_list(paese)

        for amministrazione in lista_admin2[1].iteritems():
            code_admin = amministrazione[0]
            nome_admin = amministrazione[1]['name_clean']

            # all_codes = aree_amministrative.livelli_amministrativi_0_1(code_admin)
            # self.area_messaggi.insert(INSERT, all_codes)

            db_conn_landslide.file_structure_creation(nome_admin, code_admin)
            newLandslideAssessment = completeLandslide.HazardAssessmentLandslide(self.dbname, self.user, self.password)
            newLandslideAssessment.extract_poly2_admin(paese, nome_admin, code_admin)

            section_pop_raster_cut = newLandslideAssessment.cut_rasters_landslide(paese, nome_admin, code_admin)

            if section_pop_raster_cut == "sipop":
                self.area_messaggi.insert(INSERT, "Population clipped....")
            elif section_pop_raster_cut == "nopop":
                self.area_messaggi.insert(INSERT, "Population raster not available....")
                sys.exit()

        dizio_landslide = db_conn_landslide.collect_landslide_population_frequencies_frm_dbfs()
        self.area_messaggi.insert(INSERT, "Data Collected\n")
        adms = set()
        for chiave, valori in sorted(dizio_landslide.iteritems()):
            adms.add(chiave.split("-")[1])
        insert_list = db_conn_landslide.prepare_insert_statements_landslide_monthly_values(adms, dizio_landslide)[2]
        self.area_messaggi.insert(INSERT, "Data Ready for Upload in DB\n")

        if db_conn_landslide.check_if_monthly_table_landslide_exists() == '42P01':
            db_conn_landslide.create_sparc_landslide_population_month()
            db_conn_landslide.insert_landslide_in_postgresql(insert_list)

        if db_conn_landslide.check_if_monthly_table_landslide_exists() == 'exists':
            self.area_messaggi.insert(INSERT, "Table Landslide Exist\n")
            db_conn_landslide.clean_old_values_month_landslide(paese)
            db_conn_landslide.save_changes()
            db_conn_landslide.insert_landslide_in_postgresql(insert_list)

        db_conn_landslide.save_changes()
        db_conn_landslide.close_connection()
        self.area_messaggi.insert(INSERT, "Data for " + paese + " Uploaded in DB\n")

    def landslide_iso_cleaning(self,nome_paese):
        
       
        if nome_paese == "Bolivia":
            nome_paese = "Bolivia, Plurinational State of"
        elif nome_paese == "Democratic Republic of the Congo":
            nome_paese = "Congo, The Democratic Republic of the"
        elif nome_paese == "Iran":
            nome_paese = "Iran, Islamic Republic of"
        elif nome_paese == "Ivory Coast":
            nome_paese = u"Côte d'Ivoire"
        elif nome_paese == "Lao PDR":
            nome_paese = "Lao People's Democratic Republic"
        elif nome_paese == "Lao PDR":
            nome_paese = "Lao People's Democratic Republic"
        elif nome_paese == "Sao Tome and Principe":
            nome_paese = "Sao Tome and Principe"
        elif nome_paese == "Syria":
            nome_paese = "Syrian Arab Republic"
        elif nome_paese == "Tanzania":
            nome_paese = "Tanzania, United Republic of"

        iso3 = pycountry.countries.get(name=nome_paese).alpha3
        
        return iso3

    def landslide_adm2(self):

        # Metodo per il calcolo dei dati di piaggia e frana su area amministrativa 2 con correlazione
        nome_paese_per_iso = self.box_value_adm0.get()
        iso3 = self.landslide_iso_cleaning(nome_paese_per_iso)

        nuova_analisi_landslides = CIP.LandslideIncidentiPrecipitazioneAdmin2(iso3) 
        df_nasa_events = nuova_analisi_landslides.nasaEvents()
        df_nasa_events_country = df_nasa_events[df_nasa_events['iso3'] == iso3]
        df_fao_rain = nuova_analisi_landslides.faoPrecipitation()
        df_fao_rain_country = df_fao_rain[df_fao_rain['iso3'] == iso3]


        listone_giordano = {}
        if df_fao_rain.empty:
            self.area_messaggi.insert(INSERT,"No monthly distribution of precipitation...\n")
            pass
        else:
            for area_adm_code in df_fao_rain_country.index:
                print "Processing %s " % area_adm_code
                print "*******************************"
                rain_adm2, lndslds_adm2 = nuova_analisi_landslides.selezioneDatiFaoNasaSingolaAdm2(df_fao_rain_country,
                                                                                                   df_nasa_events_country,
                                                                                                   area_adm_code)

                if len(rain_adm2.shape) == 2:
                    pass
                else:
                    solo_valori_pioggia, eventi_gcl_adm2, mesi_numerici = nuova_analisi_landslides.preparazioneDFDatiFAONASASingolaAdm(
                            rain_adm2,
                            lndslds_adm2,
                            area_adm_code)

                    try:
                        associazione_pioggia_frane_normalizzata = nuova_analisi_landslides.correlazioneDFNasaFaoNormalizzazione(solo_valori_pioggia,
                                                                                    eventi_gcl_adm2,
                                                                                    mesi_numerici)
                        # print associazione_pioggia_frane_normalizzata
                        # nuova_analisi_landslides.plotCorrelatedDataNasaFao(area_adm_code, associazione_pioggia_frane_normalizzata)
                        listato = associazione_pioggia_frane_normalizzata['eventi_norm'][:].transpose().tolist()                        
                        listone_giordano[area_adm_code] = listato
                    except:
                        pass

        for chiave, valori in listone_giordano.items():
            print chiave, valori

    def landslide_adm0(self):        

        nome_paese_per_iso = self.box_value_adm0.get()
        iso3 = self.landslide_iso_cleaning(nome_paese_per_iso)
        
        nuova_analisi = CIP.LandslideIncidentiPrecipitazioneNazionale(iso3)

        rains_trmm = nuova_analisi.trmmPrecipitationByCountry()
        glcs_tot = nuova_analisi.nasaEvents()
        glcs_country = glcs_tot[glcs_tot['iso3'] == iso3]

        corr_nazionale = nuova_analisi.national_assessment(glcs_country, rains_trmm)
        corr_nazionale = corr_nazionale.set_index(['mese'])

        nazione = corr_nazionale.loc[1:,'adm0_name']
        iso = corr_nazionale.loc[1:,'adm0_code']

        print("Country: %s ISO: %s" % (nazione[1], iso[1]))

#         for x in range(1,13):
#             corr_nazionale_subset = corr_nazionale.loc[x:x+1,'d3_n':'ev_n']
#             corr_nazionale_trans = corr_nazionale_subset[0:1].transpose()

    def landslide_mensile_NASA_WB_nazionale(self):        

        nome_paese_per_iso = self.box_value_adm0.get()
        iso3 = self.landslide_iso_cleaning(nome_paese_per_iso)
        
        nuova_analisi_NASA_WB = CIP.LandslideIncidentiPrecipitazioneNazionale(iso3)
        
        la_tabella_eventi_NASA = nuova_analisi_NASA_WB.data_fetching()
        tabella_aggiustata = nuova_analisi_NASA_WB.data_cleaning(la_tabella_eventi_NASA)      
        nuova_analisi_NASA_WB.data_analysis_vizualization(tabella_aggiustata)


root = Tk()
root.title("SPARC Flood, Drought and Landslide Assessment")
app = AppSPARC(root)