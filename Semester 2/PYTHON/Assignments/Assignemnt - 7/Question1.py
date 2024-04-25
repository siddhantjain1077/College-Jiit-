import re
def symmetric(string):
    
    return string == string[::-1]

def palindrome(string):
    
    pattern = re.compile(r'\w*')
    match = pattern.match(string)
    if match and match.group() == string:
        return symmetric(string)
    return False

string = input("Enter your string: ")
if symmetric(string):
    print("The string is symmetrical.")
if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not symmetrical and/or not a palindrome.")