def sum_odd_num(n):
    odd_sum = 0
    for i in range(1, n + 1, 2):
        odd_sum += i
    return odd_sum

def main():
    n = int(input("Enter the number: "))
    result = sum_odd_num(n)
    print(f"The sum of odd numbers from 1 to {n} is {result}")

main()
