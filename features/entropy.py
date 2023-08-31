# features.py

import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class Entropy:
    @staticmethod
    def fuzzy_entropy(signal, m=10, tau=1, r=(0.2, 2)):
        fuzzEn = EH.FuzzEn(signal, m=m, tau=tau, r=r, Fx='default')
        return fuzzEn[0]
    

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

