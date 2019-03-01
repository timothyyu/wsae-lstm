# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
import copy

import sys
sys.path.append('../..')  

import pywt
from pywt import wavedec, waverec
from scipy import signal
from statsmodels.robust import mad

#Internal Imports
from wsae_lstm.utils import dictmap_load,pickle_load,pickle_save

# # Multi-level wavelet transform
#     # https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html#pywt.wavedec
# w = pywt.Wavelet('haar')
# coeffs = wavedec(data, w, level=2,axis=0)
# cA2, cD2, cD1 = coeffs
# # cA = Approximation coefficients
#     # Approximation (low pass)
# # cD = Detail coefficient(s)
#     # Detail (high pass)
#     # Detail cofficients represent the high freq part of the signal  

# http://connor-johnson.com/2016/01/24/using-pywavelets-to-remove-high-frequency-noise/
# https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html#ref-modes
# https://pywavelets.readthedocs.io/en/latest/ref/thresholding-functions.html

def waveletSmooth( x, wavelet="haar", level=2, declevel=2):
    # calculate the wavelet coefficients
    coeff = pywt.wavedec( x, wavelet, mode='periodization',level=declevel,axis=0 )
    # calculate a threshold
    sigma = mad(coeff[-level])
    #print(sigma)
    uthresh = sigma * np.sqrt( 2*np.log( len( x ) ) )
    coeff[1:] = ( pywt.threshold( i, value=uthresh, mode="hard" ) for i in coeff[1:] )
    # reconstruct the signal using the thresholded coefficients
    y = pywt.waverec( coeff, wavelet, mode='periodization',axis=0 )
    return y

def denoise_periods(dict_dataframes):
    ddi_denoised= dict() 
    for key, index_name in enumerate(dict_dataframes):
        ddi_denoised[index_name] = copy.deepcopy(dict_dataframes[index_name])
    for key, index_name in enumerate(ddi_denoised):    
        for index,value in enumerate(ddi_denoised[index_name]):
            ddi_denoised[index_name][value][1]= waveletSmooth(ddi_denoised[index_name][value][1].values)
            ddi_denoised[index_name][value][2] = waveletSmooth(ddi_denoised[index_name][value][2].values)
            ddi_denoised[index_name][value][3] = waveletSmooth(ddi_denoised[index_name][value][3].values)
    return ddi_denoised

print("denoise_dataset - Start...")
dict_dataframes_index=pickle_load(path_filename="../../data/interim/cdii_tvt_split.pickle")

#print(dict_dataframes_index.keys())
# [index data][period 1-24][train/validate/test]
    # Train [1], Validate [2], Test [3]

ddi_denoised=denoise_periods(dict_dataframes_index)
pickle_save(ddi_denoised,path_filename="../../data/interim/cdii_tvt_split_denoised")
print("denoise_dataset - Finished.")
