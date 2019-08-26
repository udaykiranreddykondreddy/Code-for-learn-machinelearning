"@Author: @learn.machinelearning"

import numpy as np 
from numpy.linalg import qr
from scipy.linalg import lu

# Python code for LU decomposition 
# Theory https://www.instagram.com/p/BtAy08dn-tZ/
matrix_A = np.array([[4, -1, 9, 3], [13, 5, 12, 8], [4, 3, 8, 12]])
result = lu(matrix_A)
print("Result of {} = {}, {}".format(matrix_A, result[0], result[1]))

# Python code for QR decomposition 
# Theory https://www.instagram.com/p/BtAy08dn-tZ/
matrix_A = np.array([[4, -1, 9, 3], [13, 5, 12, 8], [4, 3, 8, 12]])
result = qr(matrix_A)
print("Result of {} = {}, {}".format(matrix_A, result[0], result[1]))

