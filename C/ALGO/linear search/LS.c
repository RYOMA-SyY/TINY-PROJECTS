#include <stdio.h>

int main(int argc, char const *argv[])
{
    int arr[]={7,5,8,3,0,1,1,2,0,3,5,8,7};
    int n=sizeof(arr)/sizeof(arr[0]);
    int x,y=0;
    printf("hello user, what number are you looking for?\n");
    scanf("%d",&x);
    for (int i = 0; i < n; i++)
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
        printf("your number is rpeated %d times\n", y);
    }
    

    return 0;

}