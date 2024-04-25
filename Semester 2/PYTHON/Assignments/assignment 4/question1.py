def odd_even(number):
    if number % 2 == 0:
        return "Even"
        
    else:
         return "Odd"

def main():
    number = int(input("Enter the Number :"))

    result = odd_even(number)

    print(f"The number {number} is {result}")

main()