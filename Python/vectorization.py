# Vectorization in Python is a technique that speeds up code execution by performing operations on entire arrays or data structures at once, rather than iterating through individual elements using loops. This approach leverages optimized libraries like NumPy, which execute operations in C, resulting in significant performance improvements.

import numpy as np


# Slow – Python loop
result = [x**2 for x in range(1_000_000)]

# Fast – NumPy vectorized
arr = np.arange(1_000_000)
result = arr ** 2
