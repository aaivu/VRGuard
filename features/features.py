# features.py

import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class Features:
    @staticmethod
    def calculate_fuzzy_entropy(signal, m=10, tau=1, r=(0.2, 2)):
        fuzzEn = EH.FuzzEn(signal, m=m, tau=tau, r=r, Fx='default')
        return fuzzEn[0]
    
    @staticmethod
    def compute_psd(signal,fs, lower_freq=0, upper_freq=40, calc_mean=True,calc_std=True):
        frequencies, psd = welch(signal, fs=fs)
        valid_indices = (frequencies >= lower_freq) & (frequencies <= upper_freq)
        valid_frequencies = frequencies[valid_indices]

        valid_psd = psd[valid_indices]
        return valid_psd


    @staticmethod
    def extract_pqrst(ecg_signal,fs,rpeaks=True, ppeaks=True):
        signals=ecg_signal.values
        signals = list(filter(lambda value: not np.isnan(value), signals))
        _, results = nk.ecg_peaks(signals, sampling_rate=fs)
        rpeaks = list(filter(lambda value: not np.isnan(value), results["ECG_R_Peaks"]))
        _, waves_peak = nk.ecg_delineate(signals, rpeaks, sampling_rate=fs, method="peak")
        ppeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_P_Peaks']))
        qpeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_Q_Peaks']))
        speaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_S_Peaks']))
        tpeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_T_Peaks']))  
        return [ppeaks,qpeaks, speaks, tpeaks, rpeaks]

    @staticmethod
    def rr_statistics(rr_interval, fs,mean=True, std_deviation=True):
        rr_interval = np.array(rr_interval)
        rr_interval=np.diff(rr_interval)
        rr_interval = rr_interval / fs
        if mean and std_deviation:
            return np.mean(rr_interval), np.std(rr_interval)
        elif mean:
            return np.mean(rr_interval)
        elif std_deviation:
            return np.std(rr_interval)
        else:
            return rr_interval

    #NOT YET IMPLEMENTED
    @staticmethod
    def pr_statisitics(rr_interval,pr_interval,fs,mean=True, std_deviation=True):
        rr_interval = np.array(rr_interval)
        pr_interval = np.array(pr_interval)

        if mean and std_deviation:
            return np.mean(rr_interval), np.std(rr_interval)
        elif mean:
            return np.mean(rr_interval)
        elif std_deviation:
            return np.std(rr_interval)
        else:
            return rr_interval

