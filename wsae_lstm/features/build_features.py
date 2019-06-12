#Imports (External)
import sys
sys.path.append('../..')  
#Internal Imports
from wsae_lstm import pickle_load,pickle_save
from wsae_lstm import scale_periods,denoise_periods

print("scale_dataset - Start...")
dict_dataframes_index=pickle_load(path_filename="../../data/interim/cdii_tvt_split.pickle")
ddi_scaled = scale_periods(dict_dataframes_index)
pickle_save(ddi_scaled,path_filename="../../data/interim/cdii_tvt_split_scaled")
print("scale_dataset - Finished.")

print("denoise_dataset - Start...")
ddi_scaled=pickle_load(path_filename="../../data/interim/cdii_tvt_split_scaled.pickle")
ddi_denoised= denoise_periods(ddi_scaled)
pickle_save(ddi_denoised,path_filename="../../data/interim/cdii_tvt_split_scaled_denoised")
print("denoise_dataset - Finished.")

#print(dict_dataframes_index.keys())
# [index data][period 1-24][train/validate/test]
    # Train [1], Validate [2], Test [3]



