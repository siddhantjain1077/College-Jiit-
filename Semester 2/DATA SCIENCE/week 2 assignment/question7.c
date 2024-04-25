#include <stdio.h>


int isUpperTriangular(int mat[][100], int rows, int cols) {
    
    for (int i = 1; i < rows; i++) {
        for (int j = 0; j < i && j < cols; j++) {
            
            if (mat[i][j] != 0) {
                return 0; 
            }
        }
    }
    return 1;
}

int main() {
    int mat[100][100];
    int rows, cols;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);

    printf("Enter the matrix elements:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Enter element mat[%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }

    if (isUpperTriangular(mat, rows, cols)) {
        printf("The matrix is upper triangular.\n");
    } else {
        printf("The matrix is not upper triangular.\n");
    }

    return 0;
}
