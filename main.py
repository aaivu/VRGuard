# Usage
from feature_extractor.extract_1d_signal import FeatureExtractor_1D
import pandas as pd


if __name__ == "__main__":
    signals = pd.read_csv("C:\\Users\\USER\\Desktop\\Privacy_Re\\SAMPLES\\abalation_external\\raw_data\\ecg.csv", index_col=0)
    signals=signals.iloc[0:2]
    feature_extractor = FeatureExtractor_1D(fs=500, batch_size=100)
    extracted_features = feature_extractor.extract_features(signals)
    #print(extracted_features.head())
    # You can now work with the extracted_features DataFrame
