import pandas as pd
import pickle
from sklearn import linear_model

#loading and separating our wine dataset into labels and features
df = pd.read_csv('winequality-red.csv', delimiter=";")
label = df['quality']
features = df.drop('quality', axis=1)

#defining our linear regression estimator and training it with our wine data
regr = linear_model.LinearRegression()
regr.fit(features, label)

#using our trained model to predict a fake wine
#each number represents a feature like pH, acidity, etc.
print (regr.predict([[7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4]]).tolist() )

#serializing our model to a file called model.pkl
pickle.dump(regr, open("lnModel.pkl","wb"))
#loading a model from a file called model.pkl
model = pickle.load(open("lnModel.pkl","r"))