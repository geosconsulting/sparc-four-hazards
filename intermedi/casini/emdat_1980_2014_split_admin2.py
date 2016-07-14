__author__ = 'silvia.calo'
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import pylab
import os
import unicodedata
import re
import collections
import xlwt
import itertools
from operator import itemgetter
from copy import deepcopy

#load emdat data to split the locations
emdat = pd.io.excel.read_excel("EMDAT_database_1980_2014.xls")
emdat_data = emdat[['start','end','country','location','type','subtype','killed','total_affected','est_damage','disaster_n']]
# consider only tropical cyclones
tropical_cyclones = emdat_data[emdat_data['subtype']=='Tropical cyclone']


#split the locations according to ',' '(' '/' ')' ';' ' and ' '-' '+'
import split_location
tropical_cyclones_splittato = split_location.luoghi(tropical_cyclones)

#export file "tropical_cyclones_splittato" in a csv file
tropical_cyclones_splittato.to_csv("tropical_cyclones_splittato.csv",sep = ",")

#LOAD emdat records
def load_emdat_file():
    emdat_record = {}
    with open("tropical_cyclones_splittato.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                country_name = row[3]
                if country_name in emdat_record:
                    emdat_record[country_name] = emdat_record[country_name] + [row]
                else:
                    emdat_record[country_name] = [row]
            count += 1
    return emdat_record
emdat_record = load_emdat_file()
#transform all the letters in low letters
emdat_record_lower = []
emdat_record_lower = [[x.lower() for x in item] for item in emdat_record]
#remove unusual characters
for row in range(0,len(emdat_record_lower)):
    for item in range(0,len(emdat_record_lower[row])):
        no_dash = re.sub('-', '', emdat_record_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        emdat_record_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#LOAD the file with GAUL and GADM names for all Admin areas
def load_admin_n_name():
    admin_n_name = {}
    with open("admin_n_name.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                GAUL_name = row[4]

                if GAUL_name in PHL_admin2:
                    admin_n_name[GAUL_name] = admin_n_name[GAUL_name] + [row[1]]
                else:
                    admin_n_name[GAUL_name] = [row[1]]
            count += 1
    return admin_n_name
admin_n_name = load_admin_n_name()
#transform all the letters in low letters
admin_n_name_lower = []
admin_n_name_lower = [[x.lower() for x in item] for item in admin_n_name]
#remove unusual characters
for row in range(0,len(admin_n_name_lower)):
    for item in range(0,len(admin_n_name_lower[row])):
        no_dash = re.sub('-', '', admin_n_name_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        admin_n_name_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#LOAD the file with GAUL names + ISO code
def load_gaul_wfp_iso():
    gaul_wfp_iso = {}
    with open("gaul_wfp_iso.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                GAUL_name = row[4]

                if GAUL_name in gaul_wfp_iso:
                    gaul_wfp_iso[GAUL_name] = gaul_wfp_iso[GAUL_name] + [row[1]]
                else:
                    gaul_wfp_iso[GAUL_name] = [row[1]]
            count += 1
    return gaul_wfp_iso
gaul_wfp_iso = load_gaul_wfp_iso()

#transform all the letters in low letters
gaul_wfp_iso_lower = []
gaul_wfp_iso_lower = [[x.lower() for x in item] for item in gaul_wfp_iso]
#remove unusual characters
for row in range(0,len(gaul_wfp_iso_lower)):
    for item in range(0,len(gaul_wfp_iso_lower[row])):
        no_dash = re.sub('-', '', gaul_wfp_iso_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        gaul_wfp_iso_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#correct the ISO code gadm using Fabio's table "gaul_wfp_iso"
for i in range(0,len(admin_n_name_lower)):
    for j in range(0,len(gaul_wfp_iso_lower)):
        if admin_n_name_lower[i][11]==gaul_wfp_iso_lower[j][10]:
            admin_n_name_lower[i][12]=gaul_wfp_iso_lower[j][16]

#LOAD the file with GAUL and GADM names for the Admin0 areas
def load_admin0_name():
    admin0_name_GADM_GAUL = {}
    with open("admin0_name_GADM_GAUL.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                GAUL_name0 = row[4]

                if GAUL_name0 in PHL_admin2:
                    admin0_name_GADM_GAUL[GAUL_name0] = admin0_name_GADM_GAUL[GAUL_name0] + [row[1]]
                else:
                    admin0_name_GADM_GAUL[GAUL_name0] = [row[1]]
            count += 1
    return admin0_name_GADM_GAUL
admin0_name_GADM_GAUL = load_admin0_name()
#transform all the letters in low letters
admin0_name_GADM_GAUL_lower = []
admin0_name_GADM_GAUL_lower = [[x.lower() for x in item] for item in admin0_name_GADM_GAUL]
#remove unusual characters
for row in range(0,len(admin0_name_GADM_GAUL_lower)):
    for item in range(0,len(admin0_name_GADM_GAUL_lower[row])):
        no_dash = re.sub('-', '', admin0_name_GADM_GAUL_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        admin0_name_GADM_GAUL_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#LOAD pop_admin0_FAO
def load_pop_admin0_FAO():
    pop_admin0_FAO = {}
    with open("FAOSTAT_population_data_v2.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                country_name = row[3]
                if country_name in pop_2011_admin2:
                    pop_admin0_FAO[country_name] = pop_admin0_FAO[country_name] + [row]
                else:
                    pop_admin0_FAO[country_name] = [row]
            count += 1
    return pop_admin0_FAO
pop_admin0_FAO = load_pop_admin0_FAO()
#transform all the letters in low letters
pop_admin0_FAO_lower = []
pop_admin0_FAO_lower = [[x.lower() for x in item] for item in pop_admin0_FAO]
#remove unusual characters
for row in range(0,len(pop_admin0_FAO_lower)):
    for item in range(0,len(pop_admin0_FAO_lower[row])):
        no_dash = re.sub('-', '', pop_admin0_FAO_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        pop_admin0_FAO_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#LOAD population_2011_admin2
def load_pop_2011_admin2():
    pop_2011_admin2 = {}
    with open("population_2011_admin2.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                country_name = row[3]
                if country_name in pop_2011_admin2:
                    pop_2011_admin2[country_name] = pop_2011_admin2[country_name] + [row]
                else:
                    pop_2011_admin2[country_name] = [row]
            count += 1
    return pop_2011_admin2
pop_2011_admin2 = load_pop_2011_admin2()
#transform all the letters in low letters
pop_2011_admin2_lower = []
pop_2011_admin2_lower = [[x.lower() for x in item] for item in pop_2011_admin2]
#remove unusual characters
for row in range(0,len(pop_2011_admin2_lower)):
    for item in range(0,len(pop_2011_admin2_lower[row])):
        no_dash = re.sub('-', '', pop_2011_admin2_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        pop_2011_admin2_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#LOAD population_2011_admin0
def load_pop_2011_admin0():
    pop_2011_admin0 = {}
    with open("population_2011_admin0.csv", 'rb') as f:
        tmp = csv.reader(f)
        return [[x.strip() for x in row] for row in tmp]    #delete white spaces before and after the word
        count = 0.0
        for row in tmp:
            if count > 0:  # Misses Header Rows
                country_name = row[3]
                if country_name in pop_2011_admin0:
                    pop_2011_admin0[country_name] = pop_2011_admin0[country_name] + [row]
                else:
                    pop_2011_admin0[country_name] = [row]
            count += 1
    return pop_2011_admin0
pop_2011_admin0 = load_pop_2011_admin0()
#transform all the letters in low letters
pop_2011_admin0_lower = []
pop_2011_admin0_lower = [[x.lower() for x in item] for item in pop_2011_admin0]
#remove unusual characters
for row in range(0,len(pop_2011_admin0_lower)):
    for item in range(0,len(pop_2011_admin0_lower[row])):
        no_dash = re.sub('-', '', pop_2011_admin0_lower[row][item])
        no_space = re.sub(' ', '', no_dash)
        no_slash = re.sub('/', '_', no_space)
        no_apice = re.sub('\'', '', no_slash)
        no_bad_char = re.sub(r'-/\([^)]*\)', '', no_apice)
        unicode_pulito = no_bad_char.decode('latin1')
        pop_2011_admin0_lower[row][item] = unicodedata.normalize('NFKD', unicode_pulito).encode('ascii', 'ignore')

#calculate the percentage of people that live in each admin2 area of a country
import population_admin2
pop_2011_admin2_lower = population_admin2.percentage_admin2s(pop_2011_admin2_lower,pop_2011_admin0_lower)

emdat_record_list = []
for row in emdat_record_lower[1:]:
    emdat_record_list.append(row)

#correct the names of the admin2 areas
#emdat_record_clean_out = [['34', '00_4_1980', '00_4_1980', 'bangladesh', 'storm', 'tropicalcyclone', '11.0', '1050.0', '', '19800038', ''], ['45', '1981030600:00:00', '1981030600:00:00', 'bangladesh', 'storm', 'tropicalcyclone', '15.0', '25000.0', '', '19810274', 'comilla']]
import clean_admin2_name
emdat_record_clean_out = clean_admin2_name.clean(emdat_record_list)

#correct the names of the admin2 areas (from GADM to GAUL) and the names of the admin0 names (from GADM to GAUL)
#emdat_record_clean_GAUL = [['34', '00_4_1980', '00_4_1980', 'bangladesh', 'storm', 'tropicalcyclone', '11.0', '1050.0', '', '19800038', ''], ['45', '1981030600:00:00', '1981030600:00:00', 'bangladesh', 'storm', 'tropicalcyclone', '15.0', '25000.0', '', '19810274', 'chandpur']]
import from_GADM_to_GAUL
emdat_record_clean_GAUL = from_GADM_to_GAUL.GADM_GAUL(emdat_record_clean_out,admin_n_name_lower,admin0_name_GADM_GAUL_lower)

#replace the name of the admin1 area with the name of the admin2 areas that fall inside the admin1
#emdat_record_admin2 = [['1570', '2002092000:00:00', '2002092400:00:00', 'guatemala', 'storm', 'tropicalcyclone', '2.0', '1500.0', '0.1', '20020849', 'sanmarcos', 'lareforma'], ['287', '1986051600:00:00', '1986051600:00:00', 'india', 'storm', 'tropicalcyclone', '11.0', '100.0', '', '19860062', 'rajasthan', 'ajmer']]
import convert_admin1_to_admin2
emdat_record_admin2 = convert_admin1_to_admin2.admin1_admin2(emdat_record_clean_GAUL,admin_n_name_lower)
#from the start date, keep only the year in which the cyclone occurs
for item in emdat_record_admin2:
    item[1] = item[1][0:4]



# #create a nested dictionary from a list of lists in which the first key is the country and the second key is the admin2 name. for each admin2 there are the events recorded
# #emdat_dict = {'philippines': {'camarinesnorte': [['1812', '2004112900:00:00', '2004113000:00:00', 'philippines', 'storm', 'tropicalcyclone', '1619.0', '881023.0', '78.2', '20040609', 'regionv(bicolregion)', 'camarinesnorte']],
# #'ilocossur': [['656', '1992071100:00:00', '1992071200:00:00', 'philippines', 'storm', 'tropicalcyclone', '22.0', '5135.0', '', '19920295', 'regioni(ilocosregion)', 'ilocossur']]....}
# ###INUTILE###
# pop_FAO_dict_admin0 = {}
# for row in pop_admin0_FAO_lower:
#     countries = row[3]
#     pop_year = row[8]
#     if countries not in pop_FAO_dict_admin0:
#         pop_FAO_dict_admin0[countries] = {}
#     if pop_year not in pop_FAO_dict_admin0[countries]:
#         pop_FAO_dict_admin0[countries][pop_year] = [row[11]]
#     elif row[11] not in pop_FAO_dict_admin0[countries][pop_year]:
#         pop_FAO_dict_admin0[countries][pop_year] += [row[11]]

pop_FAO_list = deepcopy(pop_admin0_FAO_lower)
for row in pop_FAO_list:
    del row[0:3]
    del row[1:5]
    del row[2:4]
    del row[3:5]

#create a dictionary with, per each admin2, the percentage of people of the relative country that live in that administrative area
perc_admin2_dict = {}
for row in pop_2011_admin2_lower:
    admin2_code = row[0]
    admin0_name = row[14]
    for row2 in pop_FAO_list:
        year = row2[1]
        if admin0_name == row2[0]:
            if year not in perc_admin2_dict:
                perc_admin2_dict[year] = {}
            if admin2_code not in perc_admin2_dict[year]:
                perc_admin2_dict[year][admin2_code] = row[18]
            elif row[18] not in perc_admin2_dict[year][admin2_code]:
                perc_admin2_dict[year][admin2_code] += row[18]
#convert the percentages from string to float
for year in perc_admin2_dict:
    for admin2_code in perc_admin2_dict[year]:
        perc_admin2_dict[year][admin2_code] = float(perc_admin2_dict[year][admin2_code])

#create a dictionary with, per each admin2, the number of inhabitants that live in the country which the admin2 belongs to
pop_admin2_dict = {}
for row in pop_2011_admin2_lower:
    admin2_code = row[0]
    admin0_name = row[14]
    for row2 in pop_FAO_list:
        year = row2[1]
        if admin0_name == row2[0]:
            if year not in pop_admin2_dict:
                pop_admin2_dict[year] = {}
            if admin2_code not in pop_admin2_dict[year]:
                pop_admin2_dict[year][admin2_code] = row2[2]
            elif row[18] not in pop_admin2_dict[year][admin2_code]:
                pop_admin2_dict[year][admin2_code] += row2[2]
#convert the percentages from string to float
for year in pop_admin2_dict:
    for admin2_code in pop_admin2_dict[year]:
        pop_admin2_dict[year][admin2_code] = float(pop_admin2_dict[year][admin2_code])

#create a dictionary with the number of inhabitants that live in each admin2, in each of the years reported by FAO
pop_admin2_year = deepcopy(pop_admin2_dict)
for year in pop_admin2_year:
    for admin2_code in pop_admin2_year[year]:
        pop_admin2_year[year][admin2_code] = pop_admin2_dict[year][admin2_code] * perc_admin2_dict[year][admin2_code]

for i in range(0,len(emdat_record_admin2)):
    emdat_record_admin2[i].append('')
#add the code of the admin2 area at the end of each item
for j in range(0,len(pop_2011_admin2_lower)):
    for i in range(0,len(emdat_record_admin2)):
        if emdat_record_admin2[i][3] == pop_2011_admin2_lower[j][14] and emdat_record_admin2[i][11] == pop_2011_admin2_lower[j][8]:
            emdat_record_admin2[i][12]= pop_2011_admin2_lower[j][0]

emdat_event = {}
for row in emdat_record_admin2:
    #year_event = row[1]
    event_code = row[9]
    if event_code not in emdat_event:
        emdat_event[event_code] = [row[12]]
    elif row[12] not in emdat_event[event_code]:
        emdat_event[event_code] += [row[12]]
#create a nested list with the code of the event and all the admin2 affected
emdat_event_list = []
for key, value in emdat_event.iteritems():
    temp = [key,value]
    emdat_event_list.append(temp)
#add to the list the year in which the event happened
for item in emdat_event_list:
    item.insert(1, item[0][0:4])

#create a nested list with the number of inhabitants that in the year of the event lived in each admin2 area affected
pop_emdat_event = deepcopy(emdat_event_list)
for year in pop_admin2_year:
    for admin2_code in pop_admin2_year[year]:
        for item in pop_emdat_event:
            for j in range(0,len(item[2])):
                if item[1]==year and item[2][j]==admin2_code:
                    item[2][j]=float(pop_admin2_year[year][admin2_code])


#create a nested list with the sum of inhabitants that in the year of the event lived in the admin2 areas affected
tot_pop_emdat_event = []
for item in pop_emdat_event:
    tot_pop_emdat_event.append([item[0]])
for item in tot_pop_emdat_event:
    item.append(item[0][0:4])
for i in range(0,len(pop_emdat_event)):
#for i in range(0,20):
    tot_pop_emdat_event[i].append('')
    if pop_emdat_event[i][0] == tot_pop_emdat_event[i][0] and pop_emdat_event[i][1] == tot_pop_emdat_event[i][1]:
       tot_pop_emdat_event[i][2]= sum(pop_emdat_event[i][2])

#create a list in which there are the percentage of people that lived in each admin2 affected
perc_emdat_event = deepcopy(pop_emdat_event)
for i in range(0, len(perc_emdat_event)):
    print perc_emdat_event[i]
    divisore = tot_pop_emdat_event[i][2]
    for j in range(0,len(perc_emdat_event[i][2])):
        dividendo = perc_emdat_event[i][2][j]
        perc_emdat_event[i][2][j] = dividendo/float(divisore)

emdat_records_no_locations = deepcopy(emdat_record_admin2)
#print emdat_records_no_locations[0:4]


# pop_emdat_event = deepcopy(emdat_event)
# for event_code in pop_emdat_event:
#     for year in emdat_event[event_code]:
#         for i in range(0,len(emdat_event[event_code][year])):
#             if emdat_event[event_code][year][i]==pop_admin2_year


workbook=xlwt.Workbook(encoding='ascii')
sheet2=workbook.add_sheet('emdat_record_match')
# sheet1=workbook.add_sheet('emdat_record_list')
# sheet3=workbook.add_sheet('emdat_record_clean_nodup')
for i in range(0,len(emdat_record_admin2)):
    for j in range(0,len(emdat_record_admin2[i])):
        sheet2.write(i,j,emdat_record_admin2[i][j])
# for i in range(0,len(emdat_record_list)):
#     for j in range(0,len(emdat_record_list[i])):
#         sheet1.write(i,j,emdat_record_list[i][j])
# for i in range(0,len(emdat_record_clean_nodup)):
#     for j in range(0,len(emdat_record_clean_nodup[i])):
#         sheet3.write(i,j,emdat_record_clean_nodup[i][j])

workbook.save('C:/data/PYTHON/python/emdat/output_1980_2014_split_admin2/emdat_record_match.xls')


