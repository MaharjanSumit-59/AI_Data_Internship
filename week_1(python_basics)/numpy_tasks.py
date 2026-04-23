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

### HARD
# Create a checkerboard pattern (like a chessboard) using NumPy.
"""
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1
print(chessboard)
"""

# Normalize an array (scale values between 0 and 1).
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print(normalized_arr)
"""
# Find the row-wise and column-wise sums of a 2D array.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
row_sum = np.sum(arr, axis=1)
column_sum = np.sum(arr, axis=0)
print(arr)
print("Row-wise sums:", row_sum)
print("Column-wise sums:", column_sum)
"""
# Compute the dot product of two matrices.
"""
arr = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr, arr2)
print(dot_product)
"""
# Find unique elements and their counts in an array.
"""
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique elements:", unique_elements)
print("Counts:", counts)
"""
# Sort an array along rows and columns separately.
"""
arr = np.array([[3, 1, 4], [6, 5, 2]])
# Sort along rows
sorted_rows = np.sort(arr, axis=1)
print("Sorted along rows:\n", sorted_rows)
# Sort along columns
sorted_columns = np.sort(arr, axis=0)
print("Sorted along columns:\n", sorted_columns)
"""
# Implement broadcasting to add a 1D array to each row of a 2D array.
"""
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[4, 5, 6], [7, 8, 9]])
result = arr_2d + arr_1d
print(result)
"""
# Replace the maximum value in each row with 0.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
# max_indices = np.argmax(arr, axis=1)
# for i in range(arr.shape[0]): 
#     arr[i, max_indices[i]] = 0 
# print(arr)
max = np.max(arr, axis=1)
for i in range(arr.shape[0]):
    arr[i, arr[i] == max[i]] = 0 # This will replace all occurrences of the maximum value in each row with 0
print(arr)
"""
# Find duplicate elements in an array.
"""
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
duplicates = arr[np.where(np.bincount(arr) > 1)]
print("Duplicate elements:", duplicates)
"""

# Create a function that computes pairwise distances between points using NumPy.
"""
def compute_pairwise_distances(points):
    
    # Compute pairwise distances between points.

    # Parameters:
    # points (numpy.ndarray): An array of shape (n, d) where n is the number of points and d is the dimensionality.

    # Returns:
    # numpy.ndarray: A matrix of shape (n, n) containing pairwise distances.
    
    # Calculate the squared differences
    squared_diff = np.sum((points[:, np.newaxis] - points) ** 2, axis=-1)
    
    # Take the square root to get the distances
    distances = np.sqrt(squared_diff)
    
    return distances

print(compute_pairwise_distances(np.array([[0, 0], [1, 1], [2, 2]])))
"""