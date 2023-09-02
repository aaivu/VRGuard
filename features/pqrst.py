
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class PQRST:
    @staticmethod
    def extract_R_peaks(ecg_signal,fs):
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
