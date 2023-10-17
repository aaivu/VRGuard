# features.py

import EntropyHub as EH
import neurokit2 as nk
import numpy as np
from scipy.signal import welch


class Entropy:
    @staticmethod
    def fuzzy_entropy(signal, m=10, tau=1, r=(0.2, 2)):
        """
        Fuzzy entropy is a measure of complexity that is based on approximate entropy, but is less sensitive to outliers
        :param signal: input signal
        :param m:  dimensionality of the fuzzy entropy to be calcualted
        :param tau:
        :param r:
        :return: array of m fuzzy entropies
        """
        fuzzEn = EH.FuzzEn(signal, m=m, tau=tau, r=r, Fx='default')
        return fuzzEn[0]
    


