#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int a,b;
    int c;
    printf("Enter the 2 Numbers :");
    scanf("%d%d",&a,&b);
    c= add(a,b);
    printf("Sum = %d",c);
}
int add(int i, int j)
{
    int sum;
    sum = i + j;
    return sum;
}



