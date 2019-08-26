"@Author: @learn.machinelearning"

import numpy as np 

# Python code for scalar * Matrix
scalar = 5
matrix_A = np.array([[4, -1, 9, 3], [1, 4, 8, 4]])
result_add = scalar * matrix_A # element wise addition
print("Result of {} * {} = {}".format(scalar, matrix_A, result_add))

# Python code for Matrix * Matrix
matrix_A = np.array([[4, 9, 6, -5], [4, 7, 1, -9]])
matrix_B = np.array([[4,4], [-1,7], [9,9], [3,1]])
result = matrix_A.dot(matrix_B)
print("Result of {} * {} = {}".format(matrix_A , matrix_B, result))
