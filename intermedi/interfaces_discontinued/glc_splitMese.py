import pandas as pd
from sqlalchemy import create_engine,MetaData
from geoalchemy2 import Geometry
import matplotlib.pyplot as plt

def data_fetching(ip_in, table_name, schema):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')

    try:
        df_in_sql = pd.read_sql_table(table_name, engine_in, schema=schema, index_col='id', parse_dates={'date': '%Y-%m-%d'})
    except Exception as e:
        print e.message

    return df_in_sql


def data_cleaning(df,iso):

    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    tabella_lavoro = df[df['iso3'] == iso]
    return tabella_lavoro

def data_analysis(iso):

    ip_in = '127.0.0.1'
    table = 'glc20160114_wfp'
    schema = "nasa"
    iso = iso
    la_tabella = data_fetching(ip_in, table, schema)
    tabella_aggiustata = data_cleaning(la_tabella, iso)
    incidenti_per_meseSerie = tabella_aggiustata.groupby(['rcl_type','month'])['month'].count()
    incidenti_per_meseDataFrame = tabella_aggiustata.groupby(['rcl_type','month']).count()

    #print incidenti_per_meseSerie
    solo_landslides = incidenti_per_meseDataFrame.loc['Landslide','iso3']
    plt.plot(solo_landslides)
    plt.title('NASA Registered Landslides')
    plt.show()


    return incidenti_per_meseSerie

if __name__ == "__main__":
    data_analysis("NPL")