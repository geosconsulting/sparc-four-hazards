__author__ = 'fabio.lana'

import pandas as pd
from sqlalchemy import create_engine, MetaData
import sys
import socket

def sqlalch_connect(ip_in, table_name):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')
    try:
        conn_in = engine_in.connect()
        metadata_in = MetaData(engine_in)
        conn = engine_in.connect()
        conn.execute("SET search_path TO public")
    except Exception as e:
        print e.message

    df_in_sql = pd.read_sql_table(table_name, engine_in, index_col='id')

    return df_in_sql


def data_analysis():


   # IP_IN = socket.gethostbyname(socket.gethostname())
   ip_in = 'localhost'
   table_name = 'sparc_population_month_drought'
   print sqlalch_connect(ip_in,table_name)

if __name__ == "__main__":
    data_analysis()
