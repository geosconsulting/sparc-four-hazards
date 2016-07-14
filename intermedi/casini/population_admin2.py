__author__ = 'silvia.calo'

def percentage_admin2s(pop_2011_admin2_lower,pop_2011_admin0_lower):

    #add at the end of each item the number of people that live in the country the admin2 belongs to
    for i in range(0,len(pop_2011_admin2_lower)):
        for j in range(0,len(pop_2011_admin0_lower)):
            if pop_2011_admin2_lower[i][13]==pop_2011_admin0_lower[j][0]:
                pop_2011_admin2_lower[i].append(pop_2011_admin0_lower[j][3])
    #calculate the percentage of people that live in each admin2 of a country
    for i in range(1,len(pop_2011_admin2_lower)):
        pop_2011_admin2_lower[i].append('')
        pop_2011_admin2_lower[i][3] = float(pop_2011_admin2_lower[i][3])
        pop_2011_admin2_lower[i][17] = float(pop_2011_admin2_lower[i][17])
        pop_2011_admin2_lower[i][18] = (pop_2011_admin2_lower[i][3]*100)/(pop_2011_admin2_lower[i][17])
        pop_2011_admin2_lower[i][18] = str(pop_2011_admin2_lower[i][18])
        pop_2011_admin2_lower[i][17] = str(pop_2011_admin2_lower[i][17])
    pop_2011_admin2_lower[0].append('')

    return pop_2011_admin2_lower