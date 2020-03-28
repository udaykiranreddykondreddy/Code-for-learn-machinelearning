"@Author: @learn.machinelearning"

import numpy as np 
from numpy.linalg import norm


# Python code for dot product 
# Theory https://www.instagram.com/p/BtAy08dn-tZ/
vector_A = np.array([[4, -1, 9, 3]])
vector_B = np.array([[1], [4], [8], [4]])
result = np.dot(vector_A, vector_B)
print("Result of {} * {} = {}".format(vector_A, vector_B, result))

# Python code for angle between two vectors
# angle = cos_inverse((vector_A . vector_B)/ |Vector_A| * |vector_B|))
vector_A = np.array([[4, 9, 6, -5]])
vector_B = np.array([[4], [7], [1], [-9]])
dot_ptoduct = np.dot(vector_A, vector_B)
norm_result =  norm(vector_A) * norm(vector_B)
result = np.arccos(dot_ptoduct / norm_result)
angle = np.degrees(result)
print("Result of angel between {}, {} = {}".format(vector_A , vector_B, angle))

