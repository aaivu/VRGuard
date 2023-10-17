
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch
import pandas as pd

class PSD:

    @staticmethod
    def mean_psd(signal,fs, lower_freq=0, upper_freq=40):
        """

        :param signal: Series
            input signal
        :param fs: int
            Sampling frequency
        :param lower_freq: int
            Lower frequency to be considered in the PSD
        :param upper_freq: int
            Upper frequency to be considered in the PSD
        :return: Float
            Mean of the PSD in the frequency range
        """
        psd=compute_psd(signal,fs, lower_freq=0, upper_freq=40)
        return np.mean(psd)

    @staticmethod
    def mean_std(signal,fs, lower_freq=0, upper_freq=40):
        """

        :param signal: Series
            input signal
        :param fs: int
            Sampling frequency
        :param lower_freq: int
            Lower frequency to be considered in the PSD
        :param upper_freq: int
            Upper frequency to be considered in the PSD
        :return: standard_deviation: FLoat
            Standard Deviation of the standard deviation of the PSD in the frequency range
        """
        psd=compute_psd(signal,fs, lower_freq=0, upper_freq=40)
        return np.std(psd)


def compute_psd(signal,fs, lower_freq=0, upper_freq=40):
    """
    Compute the PSD of a signal
    :param signal: Series
        input signal
    :param fs: int
        Sampling frequency
    :param lower_freq: int
        Lower frequency to be considered in the PSD
    :param upper_freq: int
        Upper frequency to be considered in the PSD
    :return: PSD: Array
        PSD of the signal in the frequency range
    """
    frequencies, psd = welch(signal.values, fs=fs)

    valid_indices = (frequencies >= lower_freq) & (frequencies <= upper_freq)

    valid_psd = psd[valid_indices]
    return valid_psd
