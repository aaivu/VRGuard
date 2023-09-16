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
    


