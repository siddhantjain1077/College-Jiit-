def remove_element(arr, element):

  filtered_arr = []

  for item in arr:
    if item != element:
      filtered_arr.append(item)

  return filtered_arr

my_arr = [1, 3, 4, 2, 1, 5]
element_to_remove = 1

new_arr = remove_element(my_arr, element_to_remove)


print("Original array:", my_arr)
print("Array after removing element:", new_arr)
