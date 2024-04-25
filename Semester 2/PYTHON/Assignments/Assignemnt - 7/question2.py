def reverse_words(string):
    words = string.split()
    words = words[::-1]
    return ' '.join(words)

input_string = input("Enter the String you want to enter :")
print(reverse_words(input_string))