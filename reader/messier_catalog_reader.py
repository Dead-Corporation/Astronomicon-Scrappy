import pandas as pd
from sqlalchemy import create_engine
from environment.app_variables import *

db_connection_url = "postgresql://{}:{}@{}:{}/{}".format(
    postgre_user,
    postgre_password,
    postgre_host,
    postgre_port,
    postgre_name
)
engine = create_engine(db_connection_url)


def transform_object(df):
    data = pd.DataFrame()
    temp = pd.DataFrame()
    data['messier_name'] = df['M']
    temp[['ngc', 'number', 'common_name']] = df['NGC'].str.split(' ', 2, expand=True)
    data['ngc'] = temp['ngc'] + ' ' + temp['number']
    data['common_name'] = temp['common_name']
    data['type'] = df['TYPE']
    data['cons'] = df['CONS']
    data['ra'] = df['RA']
    data['dec'] = df['DEC']
    data['mag'] = df['MAG']
    data['dist'] = df['DIST (ly)']
    data['season'] = df['VIEWING SEASON']
    data['view_difficulty'] = df['VIEWING DIFFICULTY']
    data.to_sql('objects', engine, if_exists='append', index=False)


def open_file():
    dataframe = pd.read_csv(base_dir, encoding='latin-1')
    transform_object(dataframe)


open_file()