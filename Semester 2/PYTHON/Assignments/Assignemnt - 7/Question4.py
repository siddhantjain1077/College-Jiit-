def remove_duplicates(string):
    unique_characters = set()
    result = ""

    for char in string:
        if char not in unique_characters:
            unique_characters.add(char)
            result += char

    return result

input_string = input("Enter the String you want to enter : ")

print(remove_duplicates(input_string))