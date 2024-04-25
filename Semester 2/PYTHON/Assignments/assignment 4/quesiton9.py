def countdown(n):
    if n < 0:
        return
    else:
        print(n)
        countdown(n - 1)

def main():
    number = int(input("Enter a number to start the countdown: "))
    countdown(number)

main()
