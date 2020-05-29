from xgboost import XGBClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from  exactuals.prediction import FILE
import random
from collections import defaultdict

class Prediction():
    def __init__(self, data):
        self.processors = {'A': 1, 'B': 2, 'C': 3}

        self.labels = ['payee_satisfaction', 'payor_satisfaction', 'overall_satisfaction']
        features = ['processor', 'amount', 'original_currency', 'target_currency', 'fx', 'transaction_status', 'transaction_cost', 'transaction_revenue', 'pyr_id', 'pye_id', 'ppid', 'country']
        bool_feat = ['fx', 'transaction_status']

        self.df = pd.DataFrame(columns=features[:7] + ['duration'] +features[-5:])

        for feat in features:
            self.df[feat] = pd.to_numeric(pd.Series(data[feat]))

        self.df['fx'] = 1 if self.df['fx'].item() else 0
        self.df['transaction_status'] = 1 if self.df['transaction_status'].item() else 0
        self.df['transaction_revenue'] = 1 if self.df['transaction_revenue'].item() else 0
        self.df['duration'] = random.randint(1,20)

    def predict(self):
        result = defaultdict(int)
        for processor, value in self.processors.items():
            self.df['processor'] = value
            result[processor] += self.predict_payee()
            result[processor] += self.predict_payor()
            result[processor] += self.predict_overall()
        return result
        

    def predict_payee(self):
        model = XGBClassifier()
        model.load_model(FILE.PAYEE_MODEL)
        prediction = model.predict(self.df)
        return int(prediction[0])

    def predict_payor(self):
        model = XGBClassifier()
        model.load_model(FILE.PAYOR_MODEL)
        prediction = model.predict(self.df)
        return int(prediction[0])

    def predict_overall(self):
        model = XGBClassifier()
        model.load_model(FILE.OVERALL_MODEL)
        prediction = model.predict(self.df)
        return int(prediction[0])