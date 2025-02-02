import json

import pandas as pd
import pickle
import os
    
class WhitewinePredictor:
    def __init__(self):
        self.model = None
        
    def predict_single_record(self, df):
        model_name = os.environ.get('MODEL_NAME', 'Specified environment variable is not set.')
        if self.model is None:
            self.model = pickle.load(open(model_name, 'rb'))
        y_pred = self.model.predict(df)
        print(y_pred[0])
        status = (y_pred[0] > 0.5)
        return status
