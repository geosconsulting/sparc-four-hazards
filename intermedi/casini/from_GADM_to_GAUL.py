__author__ = 'silvia.calo'
#correct the names of the admin2 areas (from GADM to GAUL)

def GADM_GAUL(emdat_record_clean_out,admin_n_name_lower,admin0_name_GADM_GAUL_lower):
    emdat_record_clean_GAUL=list(emdat_record_clean_out)
    #for loop to replace the admin2 names of gadm in EMDAT with the admin2 names of GAUL
    for i in range(0,len(emdat_record_clean_GAUL)):
        for j in range(0,len(admin_n_name_lower)):
            if emdat_record_clean_GAUL[i][3]==admin_n_name_lower[j][1] and emdat_record_clean_GAUL[i][10]==admin_n_name_lower[j][5]:
                emdat_record_clean_GAUL[i][10]=admin_n_name_lower[j][7]

    #for loop to replace the admin1 names of gadm in EMDAT with the admin1 names of GAUL
    for i in range(0,len(emdat_record_clean_GAUL)):
        for j in range(0,len(admin_n_name_lower)):
            if emdat_record_clean_GAUL[i][3]==admin_n_name_lower[j][1] and emdat_record_clean_GAUL[i][10]==admin_n_name_lower[j][3]:
                emdat_record_clean_GAUL[i][10]=admin_n_name_lower[j][9]

    #for loop to replace admin0 GADM with admin0 GAUL
    for i in range(0,len(emdat_record_clean_GAUL)):
        for j in range(0,len(admin0_name_GADM_GAUL_lower)):
            if emdat_record_clean_GAUL[i][3]==admin0_name_GADM_GAUL_lower[j][0]:
                emdat_record_clean_GAUL[i][3]=admin0_name_GADM_GAUL_lower[j][1]

    return emdat_record_clean_GAUL


