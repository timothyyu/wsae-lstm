# Split index data into 24 intervals 
    # For continous train-validate-test split
    # Save split index data in 'data/pickled' folder

# Imports (External)
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
from monthdelta import monthdelta

import xlrd
import xlsxwriter
from collections import OrderedDict
import pickle

import sys
sys.path.append('../')  
# Internal Imports
from wsae_lstm.utils import dictmap_load
from wsae_lstm.utils import interval_split,dict_interval_split
from wsae_lstm.utils import pickle_save

# Load clean data from data/interim folder
dict_dataframes_index = dictmap_load(path = "../data/interim/clean_data_index.xlsx")  
#print(dict_dataframes_index.keys())

# Split each dataframe into 24 intervals/periods for train/validate/test split
dict_df_interval = dict_interval_split(dict_dataframes_index)
#print(dict_df_interval.keys())

# Save new dict of dataframes with interval splits to disk (using pickle)
pickle_save(dict_df_interval,"../data/interim/clean_data_index_interval")