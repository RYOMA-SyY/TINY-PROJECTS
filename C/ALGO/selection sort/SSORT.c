#include <stdio.h>
int main()
{
    

    int arr[5];
    int steps = 0;
    for (int i = 0; i < 5; i++)
    {
        arr[i] = 5 - i;
    }
     for (int i = 0; i < 5; i++)
    {
        printf("arr[%d] = %d\n",i, arr[i]);
    }
    printf("after sorting\n");
for (int i = 0; i < 5 - 1; i++)
{
    int min_idx = i;
    for (int j = i + 1; j < 5; j++)
    {
        if (arr[j] < arr[min_idx])
        {
            min_idx = j;
        }
        steps++;
    }
    int temp = arr[min_idx];
    arr[min_idx] = arr[i];
    arr[i] = temp;
}
  for (int i = 0; i < 5; i++)
    {
        printf("arr[%d] = %d\n",i, arr[i]);
    }
    printf("steps = %d\n", steps);

    return 0;
}
