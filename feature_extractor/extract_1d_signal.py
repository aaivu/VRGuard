import pandas as pd
from scipy.signal import welch
import neurokit2 as nk
import numpy as np
import EntropyHub as EH
from features.entropy import Entropy
from features.psd import PSD
from features.pqrst import PQRST
from utils.utils import Utils

class FeatureExtractor_1D:
    def __init__(self, fs=100, batch_size=1):
        self.fs = fs
        self.batch_size = batch_size

    def calculate_fuzzy_entropy_batch(self, batch):
        result = batch.apply(lambda row: Entropy.fuzzy_entropy(row), axis=1)
        return result.values 


    def extract_features(self, signals,prnt=False):
        fuzzy_entropy_values = []
        for i in range(0,signals.shape[0], self.batch_size):
            batch = signals.iloc[i:i + self.batch_size,:]
            batch_fuzzy_entropy = self.calculate_fuzzy_entropy_batch(batch)
            fuzzy_entropy_values.extend(batch_fuzzy_entropy)
            if i % 100 == 0 and print:
                print("Processed {} rows".format(i))

        features=pd.DataFrame(fuzzy_entropy_values)
        features.columns=["fuzz_en{}".format(i) for i in range(1,len(fuzzy_entropy_values[0])+1)]
        features["PSD"]=signals.apply(lambda row:PSD.compute_psd(row,self.fs),axis=1)
     
        features["PSD_mean"]= features["PSD"].apply(lambda row:Utils.compute_mean(row))

        features["PSD_std"]= features["PSD"].apply(lambda row:Utils.compute_std(row))

        abc["RPeaks"]=signals.apply(lambda row: PQRST.extract_r_peaks(row,fs=200))

        print(abc.head())


        print(features.head())

        return features


