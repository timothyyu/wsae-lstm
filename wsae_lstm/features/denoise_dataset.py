# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict

import sys
sys.path.append('../..')  

import pywt
from pywt import wavedec, waverec
from scipy import signal
from statsmodels.robust import mad

#Internal Imports
from wsae_lstm.utils import dictmap_load,pickle_load,pickle_save
from wsae_lstm.models.wavelet import denoise_periods

print("denoise_dataset - Start...")
dict_dataframes_index=pickle_load(path_filename="../../data/interim/cdii_tvt_split.pickle")

#print(dict_dataframes_index.keys())
# [index data][period 1-24][train/validate/test]
    # Train [1], Validate [2], Test [3]

ddi_scaled,ddi_denoised = denoise_periods(dict_dataframes_index)
pickle_save(ddi_scaled,path_filename="../../data/interim/cdii_tvt_split_scaled")
pickle_save(ddi_denoised,path_filename="../../data/interim/cdii_tvt_split_scaled_denoised")
print("denoise_dataset - Finished.")
