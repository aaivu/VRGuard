
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch
import pandas as pd

class PSD:

    @staticmethod
    def compute_psd(signal,fs, lower_freq=0, upper_freq=40):
        #print(signal)
        frequencies, psd = welch(signal.values, fs=fs)
        
        valid_indices = (frequencies >= lower_freq) & (frequencies <= upper_freq)

        valid_psd = psd[valid_indices]
        return valid_psd

    @staticmethod
    def mean_psd(signal,fs, lower_freq=0, upper_freq=40):
        psd=compute_psd(signal,fs, lower_freq=0, upper_freq=40)
        return np.mean(psd)

    @staticmethod
    def mean_psd(signal,fs, lower_freq=0, upper_freq=40):
        psd=compute_psd(signal,fs, lower_freq=0, upper_freq=40)
        return np.std(psd)