from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score,accuracy_score,classification_report
import time


class lgbm_classifier:
    def __init__(self,random_state,n_estimators,verbose=0):
        self.random_state = random_state
        self.lgbm_classifier = LGBMClassifier(random_state=self.random_state,verbose=verbose)

    def train_model(X,y,train_test_split=0.2,time=false):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train_test_split, random_state=self.random_state )
        start_time = time.time()
        self.lgbm_classifier.fit(X_train, y_train)
        training_time = time.time() - start_time

        start_time = time.time()
        y_pred = self.lgbm_classifier.predict(X_test)
        testing_time = time.time() - start_time

        if time:
            return y_pred,training_time,testing_time
        else:
            return y_pred
        

    def predict(self,X,y):
        y_pred = self.lgbm_classifier.predict(X)
        return y_pred
    
    def accuracy(self,X,y):
        y_pred = self.rf_classifier.predict(X)
        return accuracy_score(y,y_pred)
