#include <stdio.h>
#include <stdbool.h>

int main()
{
    char M[4][3];

    printf("Enter the elements of the 4x3 matrix (row by row):\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("Enter element [%d][%d]: ", i, j);
            scanf(" %c", &M[i][j]); 
        }
    }

    printf("\nThe 4x3 matrix is:\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("[%c] ", M[i][j]);
        }
        printf("\n");
    }

    return 0;
}
