import factorial_recursiv

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial_recursiv.factorial(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
