def reverse_no(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

def main():
    number = int(input("Enter the 4-digit Number: "))

    if 1000 <= number <= 9999:
        reversed_number_value = reverse_no(number)

        print(f"The reversed number is {reversed_number_value}")
    else:
        print("Please enter a valid 4-digit number")

main()
