def square_no(number):
    squared_number = number*number
    return squared_number

def main():
    number = int(input("Enter the Number you want to be squared :"))
    result = square_no(number)
    print("The square of the number is :",result)
main()