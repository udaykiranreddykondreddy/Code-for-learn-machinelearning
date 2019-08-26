"@Author: @learn.machinelearning"

from sklearn import preprocessing
import numpy as np

# Python code for Normalization, Standardization and MinMaxScaler
# Theory https://www.instagram.com/p/BtQ4csDH083/

vector_A = np.array([[1, 181, 2, 32], [4, 100, 6, 18]])
#Normalization values
normalized_X = preprocessing.normalize(vector_A)

#Standardization value
standardized_X = preprocessing.scale(vector_A)

#MinMaxScaler value
minmax_X = preprocessing.MinMaxScaler().fit_transform(vector_A)
print("original data: ", vector_A)
print("Normalization: ", normalized_X)
print("Standardization: ", standardized_X)
print("MinMaxScaler: ", minmax_X)
