import faulthandler; faulthandler.enable()
# Imports (External)
import numpy as np
import pandas as pd
import datetime as dt
import xlrd
import xlsxwriter
from collections import OrderedDict
import copy
import pickle

import sys
sys.path.append('../')  

##Visualization/plotting imports
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.cm as cm

import pywt
from pywt import wavedec, waverec
from scipy import signal
from statsmodels.robust import mad

# Internal Imports
from wsae_lstm.utils import pickle_load,pickle_save


dict_dataframes_index=pickle_load(path_filename="../data/interim/cdii_tvt_split.pickle")
ddi_scaled=pickle_load(path_filename="../data/interim/cdii_tvt_split_scaled.pickle")
ddi_denoised=pickle_load(path_filename="../data/interim/cdii_tvt_split_scaled_denoised.pickle")

def tvt_display(dict_dataframes,ddi_scaled,ddi_denoised,fname_extended):
    for key, index_name in enumerate(dict_dataframes):
        fpath = "../reports"
        pdf = PdfPages('{}/{} {}.pdf'.format(fpath,index_name,fname_extended))

        for index,value in enumerate(dict_dataframes_index[index_name]): 
            fig, axes= plt.subplots(3, 3,constrained_layout=False,figsize=(12,12))
            fig.suptitle('{}, period: {}'.format(index_name,value))
            #fig.subplots_adjust(top=0.88)

            colormap =cm.get_cmap('tab20')
            colors = [colormap(i) for i in np.linspace(0, 1,20)]

            axes[0,0].set_prop_cycle('color', colors)
            axes[0,0].set_prop_cycle('color', colors)
            axes[0,0].set_prop_cycle('color', colors)
            axes[1,0].set_prop_cycle('color', colors)
            axes[1,1].set_prop_cycle('color', colors)
            axes[1,2].set_prop_cycle('color', colors)
            axes[2,0].set_prop_cycle('color', colors)
            axes[2,1].set_prop_cycle('color', colors)
            axes[2,2].set_prop_cycle('color', colors)

            axes[0,0].set_title('Train')
            axes[0,0].plot(dict_dataframes[index_name][value][1].values,label='train data')
            axes[0,1].set_title('Train - scaled')
            axes[0,1].plot(ddi_scaled[index_name][value][1],label='scaled train data')
            axes[0,2].set_title('Train - scaled, denoised')
            axes[0,2].plot(ddi_denoised[index_name][value][1],label='scaled, denoised train data')

            axes[1,0].set_title('Validate')
            axes[1,0].plot(dict_dataframes[index_name][value][2].values,label='validate data')
            axes[1,1].set_title('Validate - scaled')
            axes[1,1].plot(ddi_scaled[index_name][value][2],label='scaled validate data')
            axes[1,2].set_title('Validate - scaled, denoised')
            axes[1,2].plot(ddi_denoised[index_name][value][2],label='scaled,denoised validate data')

            axes[2,0].set_title('Test')
            axes[2,0].plot(dict_dataframes[index_name][value][3].values,label='test data')
            axes[2,1].set_title('Test - scaled')
            axes[2,1].plot(ddi_scaled[index_name][value][3],label='scaled test data')
            axes[2,2].set_title('Test - scaled, denoised')
            axes[2,2].plot(ddi_denoised[index_name][value][3],label='scaled,denoised test data')

            
            # handles, labels = plt.gca().get_legend_handles_labels()
            # by_label = OrderedDict(zip(labels, handles))
            # plt.legend(by_label.values(), by_label.keys())
            
            art = list(ddi_denoised[index_name][value][3].columns)
            
            axes[2,1].legend(art,loc='upper center',bbox_to_anchor=(0.5, -0.1),
                ncol=5,fancybox=True,shadow=True)
            #plt.tight_layout()
            #plt.show()
            pdf.savefig(fig,bbox_inches="tight",additional_artists=art)
            plt.close()
        pdf.close()

tvt_display(dict_dataframes_index,ddi_scaled,ddi_denoised,'tvt split scale denoise visual')    
