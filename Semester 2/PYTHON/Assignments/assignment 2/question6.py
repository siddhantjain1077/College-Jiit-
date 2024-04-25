num = input("Enter a 4-digit number: ")

if len(num) == 4 and num.isdigit():
    num = int(num)

    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    print("Reversed Number:", reversed_num)
else:
    print("Invalid input. Please enter a 4-digit number.")
