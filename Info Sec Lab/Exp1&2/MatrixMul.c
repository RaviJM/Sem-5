#include <stdio.h>
#define rows1 2
#define columns1 2
#define rows2 2
#define columns2 2

void MatrixMultiplication(int m1[rows1][columns1], int m2[rows2][columns2], int (*resultantMatrix)[columns2]){
    for (int i=0;i<rows1;i++){
        for (int j=0;j<columns2;j++){
            for (int k=0;k<columns1;k++){
                resultantMatrix[i][j] += m1[i][k] * m2[k][j];
            }
        }
    }
}

int main(){

    if (columns1 == rows2){
        
        int matrix1[rows1][columns1];
        int matrix2[rows2][columns2];
        int resultantMatrix[rows1][columns2];

        printf("Enter elements of matrix-1:\n");
        for (int i=0;i<rows1;i++){
            for (int j=0;j<columns1;j++){
                printf("Enter element[%d][%d]: ",i,j);
                scanf("%d",&matrix1[i][j]);
            }
        }

        printf("Enter elements of matrix-2:\n");
        for (int i=0;i<rows2;i++){
            for (int j=0;j<columns2;j++){
                printf("Enter element[%d][%d]: ",i,j);
                scanf("%d",&matrix2[i][j]);
            }
        }

        //initialize resultant matrix
        for (int i=0;i<rows1;i++){
            for (int j=0;j<columns2;j++){
                resultantMatrix[i][j] = 0;
            }
        }

        //multiply matrix
        MatrixMultiplication(matrix1, matrix2, resultantMatrix);


        //print resultant matrix

        for (int i=0;i<rows1;i++){
            for (int j=0;j<columns2;j++){
                printf("%d ",resultantMatrix[i][j]);
            }
            printf("\n");
        }
    }


    else{
        printf("Multiplication not possible!");
    }
}