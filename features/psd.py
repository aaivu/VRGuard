
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class PSD:

    @staticmethod
    def compute_psd(signal,fs, lower_freq=0, upper_freq=40, calc_mean=True,calc_std=True):
        frequencies, psd = welch(signal, fs=fs)
        valid_indices = (frequencies >= lower_freq) & (frequencies <= upper_freq)
        valid_frequencies = frequencies[valid_indices]
        valid_psd = psd[valid_indices]
        return valid_psd