import numpy as np

def trace_of_array(arr):
    return np.trace(arr)

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("Original Array:")
print(array)

trace = trace_of_array(array)
print("\nTrace of the array:", trace)
