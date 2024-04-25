#include<stdio.h>
#include<stdlib.h>

void printArray(int *arr, int size)
{
    printf("Array elements :");
    for (int i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
    }
    printf("\n");

}
int main(){
    int *arr;
    int initialSize, newSize;

    printf("Enter the intitial size of the array ");
    scanf("%d",&initialSize);

    arr = (int*)malloc(initialSize * sizeof(int));
    if (arr == NULL)
    {
        printf("Memory allocation using malloc failed. \n");
        return 1;
    }
    
    printf("Enter %d elements for the array :\n",initialSize);
    for (int i = 0; i < initialSize; i++)
    {
        scanf("%d",&arr[i]);
    }
    
    printf("Initial ");
    printf(arr, initialSize);

    printf("Enter the new size of the array :");
    scanf("%d", &newSize);

    arr = (int*)realloc(arr, newSize * sizeof(int));
    if (arr == NULL)
    {
        printf("Memory reallocation using realloc failed.\n");
        free(arr);
        return 1;
    }

    printf("Enter %d addiotional elements for the resized array : \n", newSize - initialSize);
    for (int i = initialSize; i < newSize; i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("Resized");
    printArray(arr,newSize);

    free(arr);
    return 0;
    
    
}
