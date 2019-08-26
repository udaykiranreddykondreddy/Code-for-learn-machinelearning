"@Author: @learn.machinelearning"
"Python code for "

import numpy as np 
# Vector Addition and Subtraction
vector_A = np.array([[4, 9, 6, -5]])
vector_B = np.array([[4, -1, 9, 3]])
result_add_vector = vector_A + vector_B # element wise addition
result_sub_vector = vector_A - vector_B
print("Result of {} + {} = {}".format(vector_A,vector_B,result_add_vector))
print("Result of {} - {} = {}".format(vector_A,vector_B,result_sub_vector))

# Scalar + Matrix
matrix_A = np.array([[4, 9], [6, -5]])
scalar = 5
result = matrix_A + scalar
print("Result of {} + {} = {}".format(scalar,matrix_A,result))
