import numpy as np

original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("1. One-dimensional NumPy array:", array_1d)

matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("\n2. 3x3 Matrix from 2 to 10:\n", matrix_3x3)

null_vector = np.zeros(10)
print("\n3. Null Vector:", null_vector)
null_vector[6] = 11
print("Updated Vector:", null_vector)

array_12_38 = np.arange(12, 38)
print("\n4. Array from 12 to 38:\n", array_12_38)

original_array = np.array([1, 2, 3, 4])
float_array = original_array.astype(float)
print("\n5. Float Array:", float_array)

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.0])
fahrenheit = (celsius * 9/5) + 32
print("\n6. Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

original = np.array([10, 20, 30])
appended = np.append(original, [40, 50, 60, 70, 80, 90])
print("\n7. Original array:", original)
print("After append:", appended)

rand_array = np.random.rand(10)
mean = np.mean(rand_array)
median = np.median(rand_array)
std_dev = np.std(rand_array)
print("\n8. Random Array:", rand_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)
print("\n9. 10x10 Random Array:\n", array_10x10)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

array_3x3x3 = np.random.rand(3, 3, 3)
print("\n10. 3x3x3 Random Array:\n", array_3x3x3)
