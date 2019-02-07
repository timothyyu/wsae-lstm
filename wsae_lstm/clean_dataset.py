# Load and clean raw dataset from 'data/raw' folder 
    # Intermediate cleaned data stored in 'data/interim' folder
    # Final cleaned data stored in 'data/processed' folder

# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
import sys
sys.path.append('../')
# Imports (Internal)  
from utils import frames_to_excel, dictmap_load, dictmap_datetime

# Load in excel file and map each excel sheet to an ordered dict
raw_xlsx_file = pd.ExcelFile("../data/raw/raw_data.xlsx")
dict_dataframes = pd.read_excel(raw_xlsx_file,sheet_name = None)
#print(type(dict_dataframes))

# Convert ordered of dataframes to regular dict
dict_dataframes = dict(dict_dataframes)
#print(type(dict_dataframes)()

# Convert all sheet names/dict keys to lowercase using list comprehension 
    # Source: https://stackoverflow.com/a/38572808
dict_dataframes = {k.lower(): v for k, v in dict_dataframes.items()}

# Print name + number of sheets in dict of dataframes:
#print("Number of sheets: ",len(dict_dataframes),"\n")
#print("\n".join(list(dict_dataframes.keys())))

# Panel A, Developing Market
    # 'csi300 index data',
    # 'csi300 index future data'
    # 'nifty 50 index data'
    # 'nifty 50 index future data'
# Panel B, Relatively Developed Market
    # 'hangseng index data'
    # 'hangseng index future data'
    # 'nikkei 225 index data'
    # 'nikkei 225 index future data'
# Panel C, Developed Market
    # 's&p500 index data'
    # 's&p500 index future data'
    # 'djia index data'
    # 'djia index future data'

# Rename all dataframe column headers in each dataframe in dict_dataframes to lowercase
for item in dict_dataframes:
    dict_dataframes[item].columns = map(str.lower, dict_dataframes[item].columns)

# Convert dict back to orderdict after reorder to match Panel A/B/C format
    # Source: https://stackoverflow.com/a/46447976
key_order = ['csi300 index data',
'csi300 index future data',
'nifty 50 index data',
'nifty 50 index future data',
'hangseng index data',
'hangseng index future data',
'nikkei 225 index data',
'nikkei 225 index future data',
's&p500 index data',
's&p500 index future data',
'djia index data',
'djia index future data',
]
list_of_tuples = [(key, dict_dataframes[key]) for key in key_order]
dict_dataframes = OrderedDict(list_of_tuples)

# Obtain information on each sheet (row and column info)
# for item in dict_dataframes:
#     # Obtain number of rows in dataframe
#     #rc=dict_dataframes[item].shape[0]
#     # Obtain number of columns in dataframe
#     #cc =  len(dict_dataframes[item].columns)
#     print ("=======================================")
#     print (item,"\n")
#     print (dict_dataframes[item].info(verbose=False))

# Drop column 'matlab_time' from all dataframes in OrderedDict + rename OHLC columns for consistency
for item in dict_dataframes:
    for subitem in dict_dataframes[item]:
        if 'matlab_time' in subitem:
            print(subitem,"Dropped from ", item)
            dict_dataframes[item].drop(subitem,axis=1, inplace=True) 
        # Rename OHLC columns for consistency
        if 'open price' in subitem:
            print(subitem,"Renamed from ", item)
            dict_dataframes[item].rename(columns={'open price':'open'},inplace=True)
        if 'high price' in subitem:
            print(subitem,"Renamed from ", item)
            dict_dataframes[item].rename(columns={'high price':'high'},inplace=True)
        if 'low price' in subitem:
            print(subitem,"Renamed from ", item)
            dict_dataframes[item].rename(columns={'low price':'low'},inplace=True)
        if 'closing price' in subitem:
            print(subitem,"Renamed from ", item)
            dict_dataframes[item].rename(columns={'closing price':'close'},inplace=True)
        if 'close price' in subitem:
            print(subitem,"Renamed from ", item)
            dict_dataframes[item].rename(columns={'close price':'close'},inplace=True)     

# Rename date/ntime columns to date + drop mislabeled matlab_time columns
dict_dataframes['csi300 index data'].rename(columns={'time':'date'},inplace=True)
dict_dataframes['csi300 index future data'].rename(columns={'num_time':'date'},inplace=True)

dict_dataframes['nifty 50 index data'].drop(columns=['ntime'],axis=1, inplace=True)
dict_dataframes['nifty 50 index future data'].drop(columns=['ntime'],axis=1, inplace=True)

dict_dataframes['hangseng index data'].drop(columns=['time'],axis=1, inplace=True)
dict_dataframes['hangseng index data'].rename(columns={'ntime':'date'},inplace=True)

dict_dataframes['hangseng index future data'].rename(columns={'ntime':'date'},inplace=True)

dict_dataframes['nikkei 225 index data'].rename(columns={'ntime':'date'},inplace=True)
dict_dataframes['nikkei 225 index data'].drop(columns=['time'],axis=1, inplace=True)

dict_dataframes['nikkei 225 index future data'].drop(columns=['time'],axis=1, inplace=True)
dict_dataframes['nikkei 225 index future data'].rename(columns={'ntime':'date'},inplace=True)

dict_dataframes['s&p500 index data'].drop(columns=['time'],axis=1, inplace=True)
dict_dataframes['s&p500 index data'].rename(columns={'ntime':'date'},inplace=True)

dict_dataframes['djia index data'].drop(columns=['time'],axis=1, inplace=True)
dict_dataframes['djia index data'].rename(columns={'ntime':'date'},inplace=True)

dict_dataframes['djia index future data'].drop(columns=['time'],axis=1, inplace=True)

# # Verify date rename + column drop/rename
# for item in dict_dataframes:
#     # Obtain number of rows in dataframe
#     rc=dict_dataframes[item].shape[0]
#     # Obtain number of columns in dataframe
#     cc =  len(dict_dataframes[item].columns)
#     print ("=======================================")
#     print (item,"\n")
#     print (dict_dataframes[item].info(verbose=False))

# Save clean data to disk - index + futures data together
frames_to_excel(dict_dataframes,"../data/interim/clean_data.xlsx")

# Save clean data to disk - index data only
key_order = ['csi300 index data',
'nifty 50 index data',
'hangseng index data',
'nikkei 225 index data',
's&p500 index data',
'djia index data',
]
frames_to_excel(dict_dataframes,"../data/interim/clean_data_index.xlsx",key_order)

# Save clean data to disk - future data only
key_order = [
'csi300 index future data',
'nifty 50 index future data',
'hangseng index future data',
'nikkei 225 index future data',
's&p500 index future data',
'djia index future data',
]
frames_to_excel(dict_dataframes,"../data/interim/clean_data_future.xlsx",key_order)

# Load in excel file with multiple sheets
    # and map each excel sheet to an ordered dict (a dict of dataframes)
# Convert date column in each dataframe in dict of dataframes 
    # to datetime object for matplotlib, and set date column as index

dict_dataframes= dictmap_load(path = "../data/interim/clean_data.xlsx")
dict_dataframes_index = dictmap_load(path = "../data/interim/clean_data_index.xlsx")   
dict_dataframes_future = dictmap_load(path = "../data/interim/clean_data_future.xlsx")
dict_dataframes = dictmap_datetime(dict_dataframes)   
dict_dataframes_index = dictmap_datetime(dict_dataframes_index)
dict_dataframes_future = dictmap_datetime(dict_dataframes_future)

# print("\n".join(list(dict_dataframes_index.keys())))
# print("\n".join(list(dict_dataframes_future.keys())))
# print(dict_dataframes_index['csi300 index data'].info())
# print(dict_dataframes_future['csi300 index future data'].info())

# Save final cleaned/processed data to `data/processed` folder
frames_to_excel(dict_dataframes,"../data/processed/clean_data.xlsx")
frames_to_excel(dict_dataframes_index,"../data/processed/clean_data_index.xlsx")
frames_to_excel(dict_dataframes_future,"../data/processed/clean_data_future.xlsx")
