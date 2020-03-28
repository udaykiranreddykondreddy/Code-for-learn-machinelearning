"@Author: @learn.machinelearning"

import numpy as np 
from scipy import stats

# Python code for Mean, Median, Mode
# Theory https://www.instagram.com/p/BtPtUJRHd16/

import numpy as np
from scipy import stats

vector_A = np.array([[1, 1, 2, 3, 4, 6, 18]])
#mean value
mean= np.mean(vector_A)

#median value
median = np.median(vector_A)

#mode value
mode= stats.mode(vector_A)
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode[1][0][0])
