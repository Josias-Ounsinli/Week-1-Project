import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from IPython.display import Image


def data_shape(df):
    print(f" There are {df.shape[0]} rows and {df.shape[1]} columns")

"""how many missing values exist or better still what is the % of missing values in the dataset?"""

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

"""Summary of the data types in the dataset"""

def data_types(df):
    t = df.dtypes.value_counts()
    return t

def missing_values_plot(df):
    plt.figure(figsize=(20,10))
    sns.heatmap(df.isna(), cbar=False)
    plt.savefig('heatmap_missing_values.png')
    Image(filename='/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/heatmap_missing_values.png')

"""Percentage of missing values per columns with missing values"""

def missing_values_colpercent(df):
    df_with_na = df[df.columns[df.isna().sum()/df.shape[0] > 0]]
    r = (df_with_na.isna().sum()/df_with_na.shape[0]).sort_values(ascending=False)
    return r

def get_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.95)
    IQ = Q3 - Q1
    outl_index = np.where(df[col] > (Q3 + 1.5*IQ))
    outl_values = []
    for ind in list(outl_index[0]):
        outl_values.append(df[col].iloc[ind])
    
    df_outl = df.loc[df[col].isin(outl_values)]

    return df_outl
    