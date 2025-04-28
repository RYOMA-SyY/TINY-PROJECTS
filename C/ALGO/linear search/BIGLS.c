#include <stdio.h>

int main(int argc, char const *argv[])
{
    int j=1000;
    int arr[1000];
   for (int i = 0; i < 1000; i++)
   {
    arr[i]=j;
    j--;
   }
  printf("hello user, what number are you looking for?\n");
    int x;
    scanf("%d",&x);
    int y=0;
    for (int i = 0; i < 1000; i++)
    {
        if (arr[i]==x)
        {
          y++;
        }
    }
    if (y==0)
    {
        printf("the number is not in the array\n");
    }
    else
    {
        printf("your number is in the array and its rpeated %d times\n", y);
    }
   
    
    return 0;
}
