# Imports (External)
import numpy as np
import sys
sys.path.append('../..')  
import pywt
from pywt import wavedec, waverec
from statsmodels.robust import mad


#Internal Imports

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
    #print("sigma: ",sigma)
    uthresh = sigma * np.sqrt( 2*np.log( len( x ) ) )
    coeff[1:] = ( pywt.threshold( i, value=uthresh, mode="hard" ) for i in coeff[1:] )
    # reconstruct the signal using the thresholded coefficients
    y = pywt.waverec( coeff, wavelet, mode='periodization',axis=0 )
   
    return y
    #return y,sigma,uthresh