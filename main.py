# Usage
from feature_extractor.extract_1d_signal import FeatureExtractor_1D
import pandas as pd


if __name__ == "__main__":
    signals = pd.read_csv("C:\\Users\\USER\\Desktop\\Privacy_Re\\eeg_validation.csv", index_col=0)
    signals=signals.iloc[0:5]
    feature_extractor = FeatureExtractor_1D(fs=200, batch_size=100)
    extracted_features = feature_extractor.extract_features(signals)
    #print(extracted_features.head())
    # You can now work with the extracted_features DataFrame
