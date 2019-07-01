# Imports (External)
import numpy as np
import pandas as pd
import copy
import sys
sys.path.append('../..')  
from sklearn import preprocessing
#Internal Imports
from utils import pickle_load,pickle_save


def scale_periods(dict_dataframes):

    ddi_scaled = dict()
    scaler_parameters_subdict = {}

    for key, index_name in enumerate(dict_dataframes):
        ddi_scaled[index_name] = copy.deepcopy(dict_dataframes[index_name])

    for key, index_name in enumerate(ddi_scaled): 

        scaler = preprocessing.RobustScaler()

        for index,value in enumerate(ddi_scaled[index_name]):
            X_train = ddi_scaled[index_name][value][1]
            X_train_scaled = scaler.fit_transform(X_train)
            X_train_scaled_df = pd.DataFrame(X_train_scaled,columns=list(X_train.columns))
            
            X_val = ddi_scaled[index_name][value][2]
            X_val_scaled = scaler.transform(X_val)
            X_val_scaled_df = pd.DataFrame(X_val_scaled,columns=list(X_val.columns))
            
            X_test = ddi_scaled[index_name][value][3]
            X_test_scaled = scaler.transform(X_test)
            X_test_scaled_df = pd.DataFrame(X_test_scaled,columns=list(X_test.columns))
            
            ddi_scaled[index_name][value][1] = X_train_scaled_df
            ddi_scaled[index_name][value][2] = X_val_scaled_df
            ddi_scaled[index_name][value][3] = X_test_scaled_df

            ddi_scaled[index_name][value]['scaler_params'] = scaler.get_params(deep=True)
        
    return ddi_scaled


dict_dataframes_index=pickle_load(path_filename="../data/interim/cdii_tvt_split.pickle")
print("scale_dataset - Start...")
ddi_scaled = scale_periods(dict_dataframes_index)
pickle_save(ddi_scaled,path_filename="../data/interim/cdii_tvt_split_scaled")
print("scale_dataset - Finished.")