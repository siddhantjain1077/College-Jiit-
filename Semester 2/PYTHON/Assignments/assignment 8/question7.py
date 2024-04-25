class NegativeNumberError(Exception):
    def __init__(self, number):
        self.message = f"Error: Negative number ({number}) is not allowed."

def read_positive_integer():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                raise NegativeNumberError(num)
            return num
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

        except NegativeNumberError as e:
            print(e.message)

if __name__ == "__main__":
    positive_integer = read_positive_integer()
    print(f"You entered: {positive_integer}")
