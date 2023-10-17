from scipy import signal
import numpy as np
class distortions():
    def __init__(self,signals):
        self.signals=signals

    def add_noise(self,mean=0,std_dev=0):
        return self.signals+np.random.normal(mean,std_dev,self.signals.shape[1])

    def vertical_scaling(self,scale=1):
        return self.signals*scale

    def horizontal_scaling(self,scale=1):
        scaled_signal = signal.resample(self.signals, np.floor(len(self.signals) * scale).astype(np.int))
        return scaled_signal

    def segmentation(self,start,end):
        return self.signals[:,start:end]