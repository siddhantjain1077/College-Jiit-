def sort_descending(arr):
  n = len(arr)

  for i in range(n - 1):

    for j in range(0, n - i - 1):
      if arr[j] < arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr

arr = [12, 11, 13, 5, 6]

sorted_arr = sort_descending(arr)
print("Sorted array in descending order:", sorted_arr)
