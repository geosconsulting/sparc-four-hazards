# -*- coding: utf-8 -*-
__author__ = 'silvia.calo'

def luoghi(tropical_cyclones):
    import pandas as pd
    import numpy as np

    #split1 considering ","
    tropical_cyclones_split = tropical_cyclones['location'].str.split(',').apply(pd.Series, 1).stack()
    tropical_cyclones_split.index = tropical_cyclones_split.index.droplevel(-1)
    tropical_cyclones_split.name = 'location'
    del tropical_cyclones['location']
    tropical_cyclones_splittato1 = tropical_cyclones.join(tropical_cyclones_split)

    #split2 considering "("
    tropical_cyclones_split2 = tropical_cyclones_splittato1['location'].str.split('(').apply(pd.Series, 1).stack()
    tropical_cyclones_split2.index = tropical_cyclones_split2.index.droplevel(-1)
    tropical_cyclones_split2.name = 'location'
    del tropical_cyclones_splittato1['location']
    tropical_cyclones_splittato2 = tropical_cyclones.join(tropical_cyclones_split2)

    #split3 considering "/"
    tropical_cyclones_split3 = tropical_cyclones_splittato2['location'].str.split('/').apply(pd.Series, 1).stack()
    tropical_cyclones_split3.index = tropical_cyclones_split3.index.droplevel(-1)
    tropical_cyclones_split3.name = 'location'
    del tropical_cyclones_splittato2['location']
    tropical_cyclones_splittato3 = tropical_cyclones.join(tropical_cyclones_split3)

    #split4 considering ")"
    tropical_cyclones_split4 = tropical_cyclones_splittato3['location'].str.split(')').apply(pd.Series, 1).stack()
    tropical_cyclones_split4.index = tropical_cyclones_split4.index.droplevel(-1)
    tropical_cyclones_split4.name = 'location'
    del tropical_cyclones_splittato3['location']
    tropical_cyclones_splittato4 = tropical_cyclones.join(tropical_cyclones_split4)

    #split5 considering ";"
    tropical_cyclones_split5 = tropical_cyclones_splittato4['location'].str.split(';').apply(pd.Series, 1).stack()
    tropical_cyclones_split5.index = tropical_cyclones_split5.index.droplevel(-1)
    tropical_cyclones_split5.name = 'location'
    del tropical_cyclones_splittato4['location']
    tropical_cyclones_splittato5 = tropical_cyclones.join(tropical_cyclones_split5)

    #split6 considering "and"
    tropical_cyclones_split6 = tropical_cyclones_splittato5['location'].str.split(' and ').apply(pd.Series, 1).stack()
    tropical_cyclones_split6.index = tropical_cyclones_split6.index.droplevel(-1)
    tropical_cyclones_split6.name = 'location'
    del tropical_cyclones_splittato5['location']
    tropical_cyclones_splittato6 = tropical_cyclones.join(tropical_cyclones_split6)

    #split6 considering "-"
    tropical_cyclones_split7 = tropical_cyclones_splittato6['location'].str.split('-').apply(pd.Series, 1).stack()
    tropical_cyclones_split7.index = tropical_cyclones_split7.index.droplevel(-1)
    tropical_cyclones_split7.name = 'location'
    del tropical_cyclones_splittato6['location']
    tropical_cyclones_splittato7 = tropical_cyclones.join(tropical_cyclones_split7)

    #split6 considering "+"
    tropical_cyclones_split8 = tropical_cyclones_splittato7['location'].str.split('+').apply(pd.Series, 1).stack()
    tropical_cyclones_split8.index = tropical_cyclones_split8.index.droplevel(-1)
    tropical_cyclones_split8.name = 'location'
    del tropical_cyclones_splittato7['location']
    tropical_cyclones_splittato8 = tropical_cyclones.join(tropical_cyclones_split8)

    tropical_cyclones_splittato = tropical_cyclones_splittato8[tropical_cyclones_splittato8['location']!='']

    return  tropical_cyclones_splittato
