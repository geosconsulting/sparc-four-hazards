__author__ = 'fabio.lana'

import pandas as pd
from sqlalchemy import create_engine, MetaData
import sys
from ipy import IP

def sqlalch_connect(ip_in, ip_out, table_name):

    engine_in = create_engine(r'postgresql://geonode:geonode@' + ip_in + '/geonode-imports')
    try:
        conn_in = engine_in.connect()
        metadata_in = MetaData(engine_in)
        conn = engine_in.connect()
        conn.execute("SET search_path TO public")
    except Exception as e:
        print e.message

    df_in_sql = pd.read_sql_table(table_name, engine_in , index_col='id')

    engine_out = create_engine(r'postgresql://geonode:geonode@' + ip_out + '/geonode-imports')
    try:
        conn_out = engine_out.connect()
    except Exception as e:
        print e.message

    df_in_sql.to_sql(table_name, engine_out, schema='public')

def data_analysis():

    if len(sys.argv)<4:
        print 'Insufficient parameters provided'
        sys.exit()
    else:
        ip_in = IP(sys.argv[1])
        ip_out = sys.argv[2]
        table_name = sys.argv[3]
        print ip_in, ip_out, table_name
        #data_fetching(IP_IN, ip_out, table_name)

if __name__ == "__main__":
    data_analysis()