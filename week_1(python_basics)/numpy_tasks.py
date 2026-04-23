import numpy as np 

### EASY

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


### MEDIUM

# Create a 5×5 identity matrix.
"""
arr = np.identity(5)
print(arr) 
"""
# Generate a random array of size 3×3 (values between 0 and 1).
"""
arr = np.random.rand(3, 3)  
print(arr)
"""
# Find the maximum and minimum values in an array.
"""
arr = np.array([[1,2,3], [4,5,6]])
max_value = np.max(arr)
min_value = np.min(arr)
print(f"Max value: {max_value}, Min value: {min_value}")
"""
# Compute the mean, median, and standard deviation of an array.
"""
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
"""
# Extract all elements greater than 10 from an array.
"""
arr = np.array([[1, 12, 3], [14, 5, 6]])
greater_than_10 = arr[arr > 10]
print(greater_than_10)
"""
# Replace all even numbers in an array with 0.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
x = arr.copy()
x[x % 2 == 0] =0
print(x)
"""
# Stack two arrays vertically and horizontally.
"""
arr = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# Vertical stack
vertical_stack = np.vstack((arr, arr2))
print("Vertical Stack:\n", vertical_stack)
# Horizontal stack
horizontal_stack = np.hstack((arr, arr2))
print("Horizontal Stack:\n", horizontal_stack)
"""
# Flatten a 2D array into 1D.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr.flatten()
print(arr)
print(flattened)
"""
# Find the indices of elements greater than a given value.
"""
arr = np.array([[1, 12, 3], [14, 5, 6]])
greater_than_10_indices = np.where(arr > 10)
print(greater_than_10_indices)
"""
# Slice a 2D array to get a specific submatrix (e.g., middle 2×2 block).
"""
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
submatrix = arr[2:4, 1:3]
print(arr)
print(submatrix)
"""