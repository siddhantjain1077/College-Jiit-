#include<stdio.h>

#define ROWS 3
#define COLS 3

int main()
{
    int arr[ROWS][COLS];

    printf("Enter %d elements for the 2D array (%dx%d) : \n",ROWS * COLS,ROWS,COLS);
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }

    printf("Even Numbers : ");
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            if (arr[i][j] % 2 == 0)
            {
                printf("%d",arr[i][j]);
            }   
        }
    }
    
    printf("\nOdd Numbers:");
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            if (arr[i][j] % 2 != 0)
            {
                printf("%d", arr[i][j]);
            }
            
        }
        
    }
    
    return 0;
}