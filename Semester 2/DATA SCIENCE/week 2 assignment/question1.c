#include <stdio.h>

int isPrime(int num)
{
    if (num <= 1)
    {
        return 0;
    }

    for (int i = 2; i <= num / 2; i++)  
    {
        if (num % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int a[n];
    printf("Enter %d integers\n", n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Prime numbers in the array are: ");
    for (int i = 0; i < n; i++)
    {
        if (isPrime(a[i]))
        {
            printf("%d ", a[i]);
        }
    }

    return 0;
}
