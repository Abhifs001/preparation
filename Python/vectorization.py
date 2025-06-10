# Vectorization in Python is a technique that speeds up code execution by performing operations on entire arrays or data structures at once, rather than iterating through individual elements using loops. This approach leverages optimized libraries like NumPy, which are designed to handle array operations efficiently


import numpy as np#calcuate square of numbers from 0 to 99 using list comprehension which is slow
arr = [i**2 for i in range(100)]

print(arr)

# Calculate square of numbers from 0 to 99 using NumPy vectorization which is fast
arr2= np.arange(100 )
arr2 = arr2 ** 2

print(arr2)

