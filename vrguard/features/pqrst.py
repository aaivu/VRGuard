
import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class PQRST:
    @staticmethod
    def extract_peaks(ecg_signal,fs):
        """
        Extract the peaks of the ECG signal
        :param ecg_signal: Series
            Input Signal
        :param fs: int
            Sampling frequency
        :return: ppeaks: Array, qpeaks: Array, speaks: Array, tpeaks: Array, rpeaks: Array
            P,Q,S,T,R Peaks of the ECG signal
        """
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
        """
        Compute the RR intervals of the ECG signal
        :param rpeaks: Array
            R peaks of the ECG signal
        :param fs: int
            Sampling frequency
        :return: rr_interval: Array
            RR intervals of the ECG signal
        """
        return np.diff(rpeaks)/fs

    @staticmethod
    def rr_mean(r_peaks,fs):
        """
        Compute the mean of the RR intervals of the ECG signal
        :param r_peaks: Array
            R peaks of the ECG signal
        :param fs: int
            Sampling frequency
        :return: rr_mean: Float
            Mean of the RR intervals of the ECG signal
        """
        interval=PQRST.rr_interval(r_peaks,fs)
        return np.mean(interval)
    @staticmethod
    def rr_std(r_peaks,fs):
        """
        Compute the standard deviation of the RR intervals of the ECG signal
        :param r_peaks: Array
            R peaks of the ECG signal
        :param fs:  int
            Sampling frequency
        :return: rr_std: Float
            Standard deviation of the RR intervals of the ECG signal
        """
        interval=PQRST.rr_interval(r_peaks,fs)
        return np.std(interval)

    @staticmethod
    def pr_interval(ppeaks,rpeaks,fs):
        """
        Compute the PR intervals of the ECG signal
        :param ppeaks:  Array
            P peaks of the ECG signal
        :param rpeaks:  Array
            R peaks of the ECG signal
        :param fs:  int
            Sampling frequency
        :return: interval: Array
            PR intervals of the ECG signal
        """
        if len(rpeaks)>len(ppeaks):
            rpeaks=rpeaks[0:len(ppeaks)]
        elif len(rpeaks)<len(ppeaks):
            ppeaks=ppeaks[0:len(rpeaks)]
        interval = np.array(rpeaks) - np.array(ppeaks)
        interval=interval/fs
        return interval

    @staticmethod
    def pr_mean(ppeaks,rpeaks,fs):
        """
        Compute the mean of the PR intervals of the ECG signal
        :param ppeaks:  Array
            P peaks of the ECG signal
        :param rpeaks:  Array
            R peaks of the ECG signal
        :param fs:  int
            Sampling frequency
        :return:    pr_mean: Float
            Mean of the PR intervals of the ECG signal
        """
        interval=PQRST.pr_interval(ppeaks,rpeaks,fs)
        return np.mean(interval)

    @staticmethod
    def pr_std(ppeaks,rpeaks,fs):
        """
        Compute the standard deviation of the PR intervals of the ECG signal
        :param ppeaks:  Array
            P peaks of the ECG signal
        :param rpeaks:  Array
            R peaks of the ECG signal
        :param fs:  int
            Sampling frequency
        :return:    pr_std: Float
            Standard deviation of the PR intervals of the ECG signal 
        """
        interval=PQRST.pr_interval(ppeaks,rpeaks,fs)
        return np.std(interval)



