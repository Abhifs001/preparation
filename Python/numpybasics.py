import numpy as np

matrix= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr = np.array([1, 2, 3, 4, 5])

# print(matrix.dtype)
# print(matrix.shape)
# print(matrix.ndim)

product = np.dot(matrix,matrix.T)

print(product)