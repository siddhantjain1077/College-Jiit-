def sum_of_first_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_first_n(n - 1)

def main():
    num = int(input("Enter a number (n) to calculate the sum of the first n numbers: "))
    result = sum_of_first_n(num)
    print(f"The sum of the first {num} numbers is: {result}")

main()
