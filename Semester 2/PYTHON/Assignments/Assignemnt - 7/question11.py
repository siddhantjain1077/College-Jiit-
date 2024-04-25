def multiply_matrices(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2):
    raise ValueError("Incompatible matrix dimensions for multiplication.")

  rows1, cols1 = len(matrix1), len(matrix1[0])
  rows2, cols2 = len(matrix2), len(matrix2[0])
  result = [[0 for _ in range(cols2)] for _ in range(rows1)] 
  for i in range(rows1):
    for j in range(cols2):
      for k in range(cols1):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

  return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
product_matrix = multiply_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
  print(row)

print("\nMatrix 2:")
for row in matrix2:
  print(row)

print("\nProduct Matrix:")
for row in product_matrix:
  print(row)
