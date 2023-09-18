
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class PQRST:
    @staticmethod
    def extract_peaks(ecg_signal,fs):
        signals=ecg_signal.values
        signals = list(filter(lambda value: not np.isnan(value), signals))
        _, results = nk.ecg_peaks(signals, sampling_rate=fs)
        rpeaks = list(filter(lambda value: not np.isnan(value), results["ECG_R_Peaks"]))
        _, waves_peak = nk.ecg_delineate(signals, rpeaks, sampling_rate=fs, method="peak")
        ppeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_P_Peaks']))
        qpeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_Q_Peaks']))
        speaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_S_Peaks']))
        tpeaks=list(filter(lambda value: not np.isnan(value), waves_peak['ECG_T_Peaks']))  
        return ppeaks,qpeaks,speaks,tpeaks,rpeaks

    @staticmethod
    def rr_interval(rpeaks,fs):
        return np.diff(rpeaks)/fs

    @staticmethod
    def rr_mean(r_peaks,fs):
        interval=PQRST.rr_interval(r_peaks,fs)
        return np.mean(interval)
    @staticmethod
    def rr_std(r_peaks,fs):
        interval=PQRST.rr_interval(r_peaks,fs)
        return np.std(interval)

    @staticmethod
    def pr_interval(ppeaks,rpeaks,fs):
        if len(rpeaks)>len(ppeaks):
            rpeaks=rpeaks[0:len(ppeaks)]
        elif len(rpeaks)<len(ppeaks):
            ppeaks=ppeaks[0:len(rpeaks)]
        interval = np.array(rpeaks) - np.array(ppeaks)
        interval=interval/fs
        return interval

    @staticmethod
    def pr_mean(ppeaks,rpeaks,fs):
        interval=PQRST.pr_interval(ppeaks,rpeaks,fs)
        return np.mean(interval)

    @staticmethod
    def pr_std(ppeaks,rpeaks,fs):
        interval=PQRST.pr_interval(ppeaks,rpeaks,fs)
        return np.std(interval)



