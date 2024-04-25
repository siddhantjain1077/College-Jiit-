def find_first_occurrence(arr, element):

  for i in range(len(arr)):
    if arr[i] == element:
      return i
  return -1

my_arr = [5, 2, 8, 2, 1]
element_to_find = 2

first_occurrence = find_first_occurrence(my_arr, element_to_find)

if first_occurrence != -1:
  print("Element", element_to_find, "found at index", first_occurrence)
else:
  print("Element", element_to_find, "not found in the array")
