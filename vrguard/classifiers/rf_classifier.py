from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score,accuracy_score,classification_report
import time


class rf_classifier:
    def __init__(self,random_state,n_estimators):
        self.random_state = random_state
        self. rf_classifier = RandomForestClassifier(random_state=self.random_state ,n_estimators=n_estimators)

    def train_model(self,X,y,test_size=0.2, calc_time=False):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=self.random_state )
        
        start_time = time.time()
        self.rf_classifier.fit(X_train, y_train)
        training_time = time.time() - start_time

        start_time = time.time()
        y_pred = self.rf_classifier.predict(X_test)
        testing_time = time.time() - start_time

        test_accuracy=accuracy_score(y_test,y_pred)
        
        if calc_time:
            return test_accuracy,training_time,testing_time
        else:
            return test_accuracy

    def predict(self,X,y):
        y_pred = self.rf_classifier.predict(X)
        return y_pred
    
    def accuracy(self,X,y):
        y_pred = self.rf_classifier.predict(X)
        return accuracy_score(y,y_pred)