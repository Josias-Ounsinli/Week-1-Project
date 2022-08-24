import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def scaler(df):
    minmax_scaler = MinMaxScaler()
    scaled = minmax_scaler.fit_transform(df)
    scaled_df = pd.DataFrame(scaled, index=df.index, columns=df.columns)
    return scaled_df


def convert_to_datetime(df, col):
    """
    convert column to datetime
    """
    df[col] = pd.to_datetime(df[col])
    return df

def fill_missing_non_numeric(df, col):
    df[col] = df[col].fillna(df[col].mode()[0])
    return df

""" drop columns with more than 30% missing values"""

def drop_columns_with_much_na(df):
    df_nona = df[df.columns[df.isna().sum()/df.shape[0] < 0.30]]
    return df_nona

def fill_missing_numeric(df, col):
    skew = df[col].skew()
    if skew > -0.05 or skew < 0.05:
        df[col] = df[col].fillna(df[col].mean())
    else:
       df[col] = df[col].fillna(df[col].median()) 
    return df
