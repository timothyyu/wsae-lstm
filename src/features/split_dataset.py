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
sys.path.append('../../')  
# Internal Imports
from utils import dictmap_load
from utils import interval_split,dict_interval_split
from utils import pickle_load,pickle_save
from utils import tvt_split,dict_df_tvt_split,dd_tvt_split

print("split_dataset - Start...")

# Load clean data from data/interim folder
dict_dataframes_index = dictmap_load(path = "../data/interim/clean_data_index.xlsx")  
#print(dict_dataframes_index.keys())

# Split each dataframe into 24 intervals/periods for train/validate/test split
dict_df_interval = dict_interval_split(dict_dataframes_index)
#print(dict_df_interval.keys())

# Save new dict of dataframes with interval splits to disk (using pickle)
pickle_save(dict_df_interval,"../data/interim/clean_data_index_interval")

# Split dataset into train-validate-test intervals per split interval
    # Save to disk as `cdii_tvt_split.pickle`
dict_dataframes_index = pickle_load(path_filename="../data/interim/clean_data_index_interval.pickle")
tvt_split_df = dd_tvt_split(dict_dataframes_index)
pickle_save(tvt_split_df,"../data/interim/cdii_tvt_split")

print("split_dataset - Finished.")