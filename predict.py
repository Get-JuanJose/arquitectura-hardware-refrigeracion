import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset2 = pd.read_csv('data.csv')
X2 = dataset2.iloc[:, :-1].values
y2 = dataset2.iloc[:, 1].values


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
 
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)

from sklearn import preprocessing
le_x = preprocessing.LabelEncoder()
X2[:,0] = le_x.fit_transform(X2[:,0])


from sklearn.model_selection import train_test_split
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regression2 = LinearRegression()
regression2.fit(X_train2, y_train2)


plt.scatter(X_test2, y_test2, color = "red")
plt.plot(X_test2, regression2.predict(X_test2), color = "blue")
plt.title("date vs temperature test data")
plt.xlabel("date")
plt.ylabel("temperature")
plt.show()

plt.scatter(X_train2, y_train2, color = "red")
plt.plot(X_train2, regression2.predict(X_train2), color = "blue")
plt.title("date vs temperature train data")
plt.xlabel("date")
plt.ylabel("temperature")
plt.show()