import pandas as pd
from IPython.display import Image

import clean_transform as transf
import dataset_infos


def load_data():
    df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Week1_challenge_data_source(CSV).csv')
    return df


def clean_data(df):
    ## Drop columns with more that 30% missing values: they are not interesting
    df = transf.drop_columns_with_much_na(df)
    for col in ['Start', 'End']:
        df = transf.convert_to_datetime(df, col)
    for col in df.select_dtypes('object').columns:
        df = transf.fill_missing_non_numeric(df, col)
    df = df.dropna(subset=['Bearer Id'])
    for col in df.select_dtypes('float').columns:
        df = transf.fill_missing_numeric(df, col)
    
    return df

def data_infos(df) -> None:
    dataset_infos.data_shape(df)
    dataset_infos.percent_missing(df)
