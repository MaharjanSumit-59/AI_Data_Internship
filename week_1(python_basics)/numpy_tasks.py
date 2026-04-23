import numpy as np 

# Create a NumPy array with values from 0 to 9.
"""
array = np.arange(10)
print(array)
"""

# Create a 3×3 array filled with zeros.
"""
array = np.zeros((3, 3))
print(array)
"""

# Create a 2×4 array filled with ones.
"""
arr = np.ones((2, 4))
print(arr)
"""

# Find the shape and dimension (ndim) of an array.
"""
arr = np.array([[1,2,3], [3,4,5]])
print("Shape:", arr.shape)
print("Dimension (ndim):", arr.ndim)
"""

# Access the last element of an array.
"""
arr = np.arange(10)
print(arr[-1])
"""
# Create an array of even numbers from 2 to 20.
"""
# arr = np.arange(2,21,2)
arr = np.arange(21)
x = arr[(arr % 2 == 0) & (arr > 0)]
print(x)
"""
# Reshape a 1D array of 12 elements into a 3×4 array.
"""
arr = np.arange(12)
new_arr = arr.reshape(3, 4)
print(new_arr)
"""
# Find the data type (dtype) of an array.
"""
arr = np.array([1,2,3,'string'])
print(arr.dtype)
"""
# Perform element-wise addition of two arrays.
"""
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = arr1 + arr2
print(arr)
"""
# Multiply all elements of an array by 5.
"""
arr = np.array([[1,2,3], [4,4,5]])
arr = arr * 5
print(arr)
"""