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

        #Calculating PSD and mean
        df_=pd.DataFrame(signals.apply(lambda row:PSD.compute_psd(row,self.fs),axis=1).values)
        df_.columns=["PSD"]
        features=pd.concat([features,df_],axis=1)
        features["PSD_mean"]= features["PSD"].apply(lambda row:Utils.compute_mean(row))
        features["PSD_std"]= features["PSD"].apply(lambda row:Utils.compute_std(row))


        #Calculating RR Peaks
        dd=pd.DataFrame()
        dd=pd.DataFrame(signals.apply(lambda row: PQRST.extract_peaks(row,fs=self.fs),axis=1).values).apply(pd.Series)  
        df_split = dd[0].apply(lambda x: pd.Series(x))
        df_split.columns=["P_peaks","Q_peaks","S_peaks","T_peaks","R_peaks"]
        features = pd.concat([features, df_split], axis=1)

        #Calculating R statisitics
        features["R_mean"]=features["R_peaks"].apply(lambda row:PQRST.rr_mean(row,fs=self.fs))
        features["R_std"]=features["R_peaks"].apply(lambda row:PQRST.rr_std(row,fs=self.fs))
        features["PR_mean"]=features[["P_peaks","R_peaks"]].apply((lambda row:PQRST.pr_mean(row[0],row[1],fs=500)),axis=1)
        features["PR_std"]=features[["P_peaks","R_peaks"]].apply((lambda row:PQRST.pr_std(row[0],row[1],fs=500)),axis=1)



        #print(features.head())

        return features


