def capitalize_first_and_last_character(string):
    
    words = string.split()
    for i in range(len(words)):
        if i == 0:
            words[i] = words[i].capitalize()
        elif i == len(words) - 1:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].capitalize()
            words[i] = words[i][0].upper() + words[i][1:]
            words[i] = words[i][:-1].lower() + words[i][-1].upper()

    return ' '.join(words)

input_string = input("Enter the String :")
print(capitalize_first_and_last_character(input_string))