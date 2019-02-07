# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
import sys
sys.path.append("../")  

def frames_to_excel(dict_dataframes, path,key_order=None):
    """Save cleaned data to disk; Write dictionary of dataframes to separate sheets, within 1 file. Optional key_order kwarg for dataframe/sheet order."""
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