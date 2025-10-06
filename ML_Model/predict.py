import joblib
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print('Loaded the model')

def make_prediction(data: dict) -> float:  # we get json data from user and convert it as a dictionary
    # convert the input data to a 2D array for prediction , since ML model expects numpy array (1 sample, 8 features)
   features = np.array([
      [
            data['longitude'], data['latitude'], data['housing_median_age'],
            data['total_rooms'], data['total_bedrooms'], data['population'],
            data['households'], data['median_income']
      ]
   ])
   prediction = saved_model.predict(features)
   return prediction[0]  # return the first element of the prediction array

def make_batch_predictions(data: List[dict]) -> np.array:
   X = np.array([
      [
            x['longitude'], x['latitude'], x['housing_median_age'],
            x['total_rooms'], x['total_bedrooms'], x['population'],
            x['households'], x['median_income']
      ]
      for x in data
   ])
   predictions = saved_model.predict(X)
   return predictions