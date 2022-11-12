import pandas as pd
import sklearn 
import pickle
import numpy

class Predictor():
  def __init__(self):
    self.model = pickle.load(open('regressor_pkl', 'rb'))
  
  def processData(self, input_data):
    data = pd.read_csv(input_data)
    data = data.dropna(axis=1).reset_index(drop=True)
    return data

  def predict(self, input_data):
    data = self.processData(input_data)
    res = self.model.predict(data)
    return res

# pred = Predictor()
# print(pred.predict('testData.csv'))
