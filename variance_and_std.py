"@Author: @learn.machinelearning"

import numpy as np 

# Python code for Variance and Standard deviation
# Theory https://www.instagram.com/p/BtPtUJRHd16/

vector_A = np.array([[1, 1, 2, 3, 4, 6, 18]])
#Variance value
variance= np.var(vector_A)

#Standard deviation value
std = np.std(vector_A)
 
print("Variance: ", variance)
print("Standard deviation: ", std)
