#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr; 
    int size, newSize;


    printf("Enter the initial size of the array: ");
    scanf("%d", &size);

    arr = (int *)malloc(size * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed. Exiting.\n");
        return 1;
    }

    printf("Enter %d elements for the initial array:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nInitial Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("\nEnter the new size of the array: ");
    scanf("%d", &newSize);


    arr = (int *)realloc(arr, newSize * sizeof(int));

    if (arr == NULL) {
        printf("Memory reallocation failed. Exiting.\n");
        return 1;
    }

    printf("Enter %d elements for the resized array:\n", newSize);
    for (int i = size; i < newSize; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nResized Array:\n");
    for (int i = 0; i < newSize; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);

    return 0;
}
