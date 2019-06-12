# Imports (External)
import numpy as np
import pandas as pd
import copy
import sys
sys.path.append('../..')  
#Internal Imports
from wsae_lstm import pickle_load,pickle_save
from wsae_lstm.models.wavelet import waveletSmooth 

def denoise_periods(dict_dataframes):

    ddi_denoised= dict() 

    for key, index_name in enumerate(dict_dataframes):
        ddi_denoised[index_name] = copy.deepcopy(dict_dataframes[index_name])

    for key, index_name in enumerate(ddi_denoised): 
        for index,value in enumerate(ddi_denoised[index_name]):
            
            X_train_scaled = ddi_denoised[index_name][value][1]
            X_val_scaled = ddi_denoised[index_name][value][2]
            X_test_scaled = ddi_denoised[index_name][value][3]

            X_train_scaled_denoised_df = pd.DataFrame(waveletSmooth(X_train_scaled),columns=list(X_train_scaled.columns))      
            X_val_scaled_denoised_df = pd.DataFrame(waveletSmooth(X_val_scaled),columns=list(X_val_scaled.columns))  
            X_test_scaled_denoised_df = pd.DataFrame(waveletSmooth(X_test_scaled),columns=list(X_test_scaled.columns))      

            ddi_denoised[index_name][value][1] = X_train_scaled_denoised_df
            ddi_denoised[index_name][value][2] = X_val_scaled_denoised_df 
            ddi_denoised[index_name][value][3] = X_test_scaled_denoised_df    

    return ddi_denoised