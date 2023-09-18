class rf_classifier:
    def __init__(self):
        self. rf_classifier = RandomForestClassifier(random_state=42,n_estimators=100)

    def train_model(X,y,train_test_split=0.2):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        start_time = time.time()
        rf_classifier = RandomForestClassifier(random_state=42,n_estimators=100)
        rf_classifier.fit(X_train, y_train)
        training_time = time.time() - start_time

        start_time = time.time()
        y_pred = rf_classifier.predict(X_test)
        testing_time = time.time() - start_time

    #def predict(X,y):
