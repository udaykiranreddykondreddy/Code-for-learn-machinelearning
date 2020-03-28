"@Author: @learn.machinelearning"

import numpy as np 
from numpy.linalg import eig

# Python code for eigen decomposition 
# Theory https://www.instagram.com/p/BtFVWoxnbYi/
matrix_A = np.array([[4, -1, 9, 3], [13, 5, 12, 8], [4, 3, 8, 12], [7, 13, 8, 12]])
result = eig(matrix_A)
eigen_values = result[0] 
eigen_vectors = result[1]
print("Result of {} = {}, {}".format(matrix_A, eigen_values, eigen_vectors))

