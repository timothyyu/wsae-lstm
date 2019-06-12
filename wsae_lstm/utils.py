# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
from monthdelta import monthdelta
import pickle
import copy

import sys
sys.path.append("../")  

def frames_to_excel(dict_dataframes, path,key_order=None):
    """Save cleaned data to disk; Write dictionary of dataframes to separate sheets, within 1 file.
     Optional key_order kwarg for dataframe/sheet order."""
    # frames_to_excel() source: https://stackoverflow.com/q/51696940
    if key_order is not None:
        list_of_tuples = [(key, dict_dataframes[key]) for key in key_order]
        dict_dataframes = OrderedDict(list_of_tuples)
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    for tab_name, dframe in dict_dataframes.items():
        dframe.to_excel(writer, sheet_name=tab_name)
    writer.save() 
    
def dictmap_load(path):
    """Load in excel file with multiple sheets
    and map each excel sheet to an ordered dict (a dict of dataframes)."""
    raw_xlsx_file = pd.ExcelFile(path)
    dict_dataframes = pd.read_excel(raw_xlsx_file,sheet_name = None)
    return dict_dataframes

def dictmap_datetime(dict_dataframes):
    """Convert date column in each dataframe in dict of dataframes 
    to datetime object for matplotlib, and set date column as index."""
    for dataframe in dict_dataframes:
        dict_dataframes[dataframe]['date'] = pd.to_datetime(dict_dataframes[dataframe]['date'].astype(str), format='%Y%m%d')
        dict_dataframes[dataframe] = dict_dataframes[dataframe].set_index('date')
    return dict_dataframes

def interval_split(df):
    """Split dataframe contents into train/validate/test intervals as defined
    in Bao, Yue, Rao (2017): 24 interval split."""
    dict_dataframes = {}
    split_count = 24
    month_increment = 0
    interval_index = 1
    
    df = df.set_index(df['date'])
    while split_count > 0:
        front = df['date'][0] 
        front = front + monthdelta(month_increment)
        back = df['date'][0]+monthdelta(30) 
        back = back + monthdelta(month_increment)
        month_increment += 3
        split_count -= 1
        df_interval = pd.DataFrame(df[(df['date'] >= front) & (df['date'] <= back)])
        dict_dataframes[interval_index] = df_interval
        dict_dataframes[interval_index].drop(['date'],axis=1,inplace=True)

        interval_index += 1
        #print(front,back)
    return dict_dataframes

def dict_interval_split(dict_dataframes):
    """Apply 24-interval split to dictionary of dataframes; 
    interval_split() function applied to each dataframe in dict object. """
    subdict_dataframes = {}
    for dataframe in dict_dataframes:
        subdict_dataframes[dataframe] = interval_split(dict_dataframes[dataframe])
    return subdict_dataframes

def pickle_save(dict_dataframes,path_filename):
    filename = path_filename
    outfile = open(filename + '.pickle','wb')
    pickle.dump(dict_dataframes,outfile)
    outfile.close()

def pickle_load(path_filename):
    infile = open(path_filename,'rb')
    dict_dataframes = pickle.load(infile)
    infile.close()
    return dict_dataframes

def tvt_split(df):
    """Train-Validate-Test split of data for continous training 
    as defined in Bao et al., 2017."""
    dict_dataframes = {}
    train = df.index[0]
    validate = df.index[0] + monthdelta(24) 
    test = df.index[0] + monthdelta(27) 
    test_end = df.index[0] + monthdelta(30) 
    df_train = pd.DataFrame(df[(df.index >= train) & (df.index <= validate)])
    df_validate = pd.DataFrame(df[(df.index >= validate) & (df.index <= test)])
    df_test = pd.DataFrame(df[(df.index >= test) & (df.index <= test_end)])
    dict_dataframes ={1:df_train,2:df_validate,3:df_test}
    return dict_dataframes

def dict_df_tvt_split(df):
    """Subfunction of dd_tvt_split()."""
    subdict_dataframes = {}
    for key in df:
        subdict_dataframes[key] =tvt_split(df[key])
    return subdict_dataframes

def dd_tvt_split(dict_dataframes):
    """Train-Validate-Test split of data applied to each index dataset as defined
    in Bao et al., 2017. """
    subdict_dataframes = {}
    for key in dict_dataframes:
        #print(key)
        subdict_dataframes[key] = dict_df_tvt_split(dict_dataframes[key])
    return subdict_dataframes