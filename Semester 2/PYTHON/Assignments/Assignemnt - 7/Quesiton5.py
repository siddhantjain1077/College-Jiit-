def is_substring(main_string, sub_string):
  return sub_string in main_string

# Example usage
main_string = "My Name is Siddhant"
sub_string = "Siddhant"

if is_substring(main_string, sub_string):
  print("Substring found!")
else:
  print("Substring not found.") 
