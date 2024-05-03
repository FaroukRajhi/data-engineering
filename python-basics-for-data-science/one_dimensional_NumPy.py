"""
Contains same data types
"""

import numpy as np

a = np.array([0,1,2,3,4])

print(a[1])
print(a.size)
print(a.shape)
print(a.ndim) # Dimension number

# Indexing and slicing methods

print(a[0])
print(a[1:3]) # output [1 2]

# Basic operations

"""
Vector addition and subtraction
Is widely used operation in data science.
In NumPy, a vector is a one-dimensional array that represents a collection of elements.
These elements can be of the same data type, such as integers, floats, or strings. 
Vectors are fundamental for numerical computations in Python due to NumPy's optimized operations for arrays.
"""

# Create a vector from a list
vector1 = np.array([1, 2, 3])
print("Vector 1:", vector1)

# Create a vector using np.arange()
vector2 = np.arange(5)  # Creates an array from 0 to 4 (excluding 5)
print("Vector 2:", vector2)

# Create a vector of zeros using np.zeros()
vector3 = np.zeros(4)
print("Vector 3:", vector3)

for i in vector1:
    print(i)

# Subtraction

u=np.array([1,0])
v=np.array([0,1])

z = u - v
print(z)