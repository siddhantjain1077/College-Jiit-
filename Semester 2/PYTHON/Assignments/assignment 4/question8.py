def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    result = power(base, exponent)
    print(f"{base}^{exponent} is: {result}")

main()