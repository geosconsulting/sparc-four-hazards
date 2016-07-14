__author__ = 'fabio.lana'

import pandas as pd
from sqlalchemy import create_engine, MetaData
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def sqlAlch_connect(ip_in, table_flood, table_rain):

    engine = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')
    try:
        conn_in = engine.connect()
        metadata_in = MetaData(engine)
        conn = engine.connect()
        conn.execute("SET search_path TO public")
    except Exception as e:
        print e.message

    df_flood = pd.read_sql_table(table_flood, engine, index_col='disaster_n')
    df_rain = pd.read_sql_table(table_rain, engine, index_col='id')

    return df_flood, df_rain


def main():

    ip_in = 'localhost'
    table_floods = 'sparc_flood_emdat'
    table_rain = 'sparc_month_prec'
    il_paese = 'Benin'

    dfs = sqlAlch_connect(ip_in, table_floods, table_rain)
    dfs[0]['country_strip'] = dfs[0]['country'].map(lambda x: str(x).strip())
    dfs[0]['start_date'] = pd.to_datetime(dfs[0]['start'], format='%Y%b%d')
    dfs[0]['year'] = dfs[0]['start_date'].dt.year
    dfs[0]['month'] = dfs[0]['start_date'].dt.month
    # print dfs[0].head()
    # print dfs[0].columns.to_series().groupby(dfs[0].dtypes).groups

    tabella_emdat_returned = dfs[0][dfs[0]['country_strip'] == il_paese]
    tabella_emdat_annuale = tabella_emdat_returned.groupby(['year'])['killed', 'total_affected'].sum()
    tabella_emdat_mensile = tabella_emdat_returned.groupby(['month'])['killed', 'total_affected'].sum()
    tabella_emdat_mensile['perc'] = (tabella_emdat_mensile['killed']/tabella_emdat_mensile['total_affected'])*100
    print tabella_emdat_mensile.describe()
    print tabella_emdat_mensile
    ts = pd.Series(tabella_emdat_mensile['total_affected'])
    plt.plot(ts)
    plt.show()

    dfs[1]['country_strip'] = dfs[1]['adm0_name'].map(lambda x: str(x).strip())
    tabella_pioggia_returned = dfs[1][dfs[1]['country_strip'] == il_paese]
    # print tabella_pioggia_returned.head()


if __name__ == "__main__":
    main()
