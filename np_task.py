import numpy as np

# Create two sample tensors (2*3)
tensor_a = np.array([[1, 2, 3], [4, 5, 6]])
tensor_b = np.array([[10, 20, 30], [40, 50, 60]])

# 1-
# Element-wise addition of tensors
addition = tensor_a + tensor_b
print("addition", addition)

# Element-wise multiplication of tensors
multiplication = tensor_a * tensor_b
print()
print()
print("multiplication", multiplication)
# 2-
# Reshape a tensor
reshaped_tensor = tensor_a.reshape(3, 2)
print()
print()
print("Original Shape:", tensor_a.shape)
print("New Shape:", reshaped_tensor.shape)
print(reshaped_tensor)

# 3-
# Slicing and indexing tensors
print()
print()
tensor_c = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8], 
                     [9, 10, 11, 12]])

# Get the first two rows and the last two columns
slice_example = tensor_c[0:2, 2:4]
print()
print()

# Indexing a specific element
element = tensor_c[1, 2]  # Returns 7
print("Sliced Tensor:", slice_example)
print("element:", element)

# 4-
# Combining tensors
print()
print()

combined = np.concatenate((tensor_a, tensor_b))
print(combined)

# 5-
# Splitting tensors
split_a, split_b = np.array_split(combined, 2, axis=0)
print("split_a :", split_a)
print("split_b :", split_a)

# 6-
# Basic mathematical operations on tensors
Summation = np.sum(tensor_a)
Mean = np.mean(tensor_a)
print("Summation:", Summation)
print("Mean:", Mean)
