#include <stdio.h>

int main()
{
    int n;
    char answer[100];
    printf("Enter n : ");
    scanf("%d", &n);

    printf("\n");

    for (int i = 1; i < n + 1; i++)
    {
        if (i % 3 != 0 && i % 5 != 0)
        {
            printf("[%d]", i);
        }

        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("[FizzBuzz]");
        }
        else
        {
            if (i % 3 == 0)
            {
                printf("[Fizz]");
            }
            if (i % 5 == 0)
            {
                printf("[Buzz]");
            }
        }
    }

    return 0;
}
