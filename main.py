# Usage
from feature_extractor.extract_1d_signal import FeatureExtractor_1D
import pandas as pd
from models.rf_classifier import rf_classifier
import numpy as np
if __name__ == "__main__":
    signals = pd.read_csv("C:\\Users\\USER\\Desktop\\Privacy_Re\\SAMPLES\\abalation_external\\raw_data\\ecg.csv", index_col=0)
    signals=signals.iloc[0:5]
    feature_extractor = FeatureExtractor_1D(fs=500, batch_size=100)
    extracted_features = feature_extractor.extract_features(signals)
    extracted_features=extracted_features.drop(columns=["PSD","R_peaks","P_peaks","Q_peaks","S_peaks","T_peaks"])
    extracted_features["label"]=[int(1) for i in range(0,extracted_features.shape[0])]
    rf=rf_classifier(random_state=42,n_estimators=100)
    y=extracted_features["label"]
    extracted_features=extracted_features.drop(columns=["label"])
    accuracy=rf.train_model(extracted_features,y,test_size=0.2)
    print(accuracy)
    print(extracted_features.head())
    # You can now work with the extracted_features DataFrame
