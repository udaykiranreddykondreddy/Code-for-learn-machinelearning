"@Author: @learn.machinelearning"

import numpy as np 

# Python code for MAD and percentiles
# Theory https://www.instagram.com/p/BtQ4csDH083/

vector_A = np.array([[1, 1, 2, 3, 4, 6, 18]])
#MAD value
mad= np.median(abs(vector_A - np.median(vector_A)))

#Standard deviation value
q1 = np.percentile(vector_A, 25)  
q2 = np.percentile(vector_A, 50)  
q3 = np.percentile(vector_A, 75)  

print("Variance: ", mad)
print("25th percentile: ", q1)
print("50th percentile: ", q2)
print("75th percentile: ", q3)
