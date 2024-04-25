import prime_checker
def main():
        number = int(input("Enter a number to check if it's prime: "))
        if prime_checker.is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
        
main()