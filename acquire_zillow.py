#standard ds imports
import pandas as pd
import numpy as np
import os

#visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

#import custom modules
from env import username, password, host

#import sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

#ignore warnings
import warnings
warnings.filterwarnings("ignore")


def get_db_url(database_name):
    """
    
    """
    url = f'mysql+pymysql://{username}:{password}@{host}/{database_name}'

    return url


def get_zillow_data():
    '''
    This function reads in the Zillow data from the Codeup db
    and returns a pandas DataFrame with cbedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips
    for all Single Family Residential properties.
    '''
    
    zillow_query = '''
    SELECT bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt 
    FROM properties_2017 as pro
    INNER JOIN predictions_2017 as pre
        ON pre.id = pro.id
    LEFT JOIN propertylandusetype as plu
        ON plu.propertylandusetypeid = pro.id
    WHERE pro.propertylandusetypeid = 261;
    '''
    return pd.read_sql(zillow_query, get_db_url('zillow'))


def prep_zillow(df):
    '''
    This function takes in the zillow df
    then the data is cleaned and returned
    '''
    #change column names to be more readable
    df = df.rename(columns={'bedroomcnt':'bedrooms','bathroomcnt':'bathrooms', 'calculatedfinishedsquarefeet':'sqft', 'taxvaluedollarcnt':'home_value'})

    #drop null values- at most there were 9000 nulls (this is only 0.5% of 2.1M)
    df = df.dropna()

    #drop duplicates
    df.drop_duplicates(inplace=True)
   
    return df


def split_zillow(df):
    '''
    This function takes in the dataframe
    and splits it into train, validate, test datasets
    '''    
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=123)
    
    return train, validate, test
