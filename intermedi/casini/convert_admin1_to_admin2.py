__author__ = 'silvia.calo'
def admin1_admin2(emdat_record_clean_GAUL,admin_n_name_lower):
    import xlwt
    #copio in emdat_record_clean_admin2 solo quei termini di lista1 in cui la location indicata e un'admin1 e la copio tante volte quante sono le admin2 al suo interno.
    #al fondo della lista aggiungo anche admin_n_name_lower[j][7] in cui ci sono i nomi delle admin2
    emdat_record_clean_admin2 = []
    for i in range(0,len(emdat_record_clean_GAUL)):
        for j in range(0,len(admin_n_name_lower)):
            if emdat_record_clean_GAUL[i][3]==admin_n_name_lower[j][11] and emdat_record_clean_GAUL[i][10]==admin_n_name_lower[j][9]:
                emdat_record_clean_admin2.append([emdat_record_clean_GAUL[i][0],emdat_record_clean_GAUL[i][1],emdat_record_clean_GAUL[i][2],emdat_record_clean_GAUL[i][3],emdat_record_clean_GAUL[i][4],emdat_record_clean_GAUL[i][5],emdat_record_clean_GAUL[i][6],emdat_record_clean_GAUL[i][7],emdat_record_clean_GAUL[i][8],emdat_record_clean_GAUL[i][9],emdat_record_clean_GAUL[i][10],admin_n_name_lower[j][7]])

    #creo la emdat_record_clean_admin2_no_admin2 che e uguale alla lista emdat_record_clean_admin2 senza il nome dell'admin2. questa lista mi serve per individuare quegli eventi in cui e riportata l'admin2
    emdat_record_clean_admin2_no_admin2 = []
    for i in range(0,len(emdat_record_clean_admin2)):
        emdat_record_clean_admin2_no_admin2.append([emdat_record_clean_admin2[i][0],emdat_record_clean_admin2[i][1],emdat_record_clean_admin2[i][2],emdat_record_clean_admin2[i][3],emdat_record_clean_admin2[i][4],emdat_record_clean_admin2[i][5],emdat_record_clean_admin2[i][6],emdat_record_clean_admin2[i][7],emdat_record_clean_admin2[i][8],emdat_record_clean_admin2[i][9],emdat_record_clean_admin2[i][10]])

    #in lista events_record_admin2 salvo tutti gli eventi in cui e gia registrata l'admin2
    events_record_admin2 = []
    for i in range(0,len(emdat_record_clean_GAUL)):
        if emdat_record_clean_GAUL[i]not in emdat_record_clean_admin2_no_admin2:
            events_record_admin2.append(emdat_record_clean_GAUL[i])

    #inserisco un campo vuoto in cui inserire l'admin1 in cui e contenuta l'admin2 secondo admin_n_name_lower (nell'esempio si chiama "philippines")
    for i in range(0,len(events_record_admin2)):
        events_record_admin2[i].insert(10,'')

    #inserisco nello spazio vuoto creato precedentemente il nome dell'admin1 in cui l'admin2 e contenuta
    for i in range(0,len(events_record_admin2)):
        for j in range(0,len(admin_n_name_lower)):
            if events_record_admin2[i][3]==admin_n_name_lower[j][11] and events_record_admin2[i][11]==admin_n_name_lower[j][7]:
                events_record_admin2[i][10]=admin_n_name_lower[j][9]
                #inserisco nella lista emdat_record_clean_admin2 gli eventi in cui e riportata solo l'admin2
                emdat_record_clean_admin2.append(events_record_admin2[i])

    #remove duplicates from emdat_record_clean_admin2:
    #convert "lista3" from a list of lists into a list of tuples
    emdat_record_clean_admin2_nodup_set = set(map(tuple,emdat_record_clean_admin2))
    #convert "lista3_nodup_set" into a list of lists as before
    emdat_record_clean_admin2_nodup = map(list,emdat_record_clean_admin2_nodup_set)

    #keep only the records in which the number of affected people is reported
    emdat_record_admin2 = []
    for i in range(1,len(emdat_record_clean_admin2_nodup)):
        if emdat_record_clean_admin2_nodup[i][7]!="":
            emdat_record_admin2.append(emdat_record_clean_admin2_nodup[i])

    return emdat_record_admin2

