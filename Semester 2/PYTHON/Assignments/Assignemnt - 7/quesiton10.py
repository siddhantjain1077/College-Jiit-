import numpy as np

def reverse_rows_columns(arr):
    return arr[::-1, ::-1] 

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

reversed_arr = reverse_rows_columns(arr)

print("Original array:\n", arr)
print("Reversed array:\n", reversed_arr)
