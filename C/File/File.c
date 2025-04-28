#include <stdio.h>

int main()
{
    FILE* GE = fopen("GE.txt","a");
    char name[30];
    char Lname[30];
    printf("Enter name : ");scanf("%s",name);
    printf("Enter last name : ");scanf("%s",Lname);
    fprintf(GE,"Name : %s \nLast Name : %s \n------------------ ",name,Lname);
    printf("\n");



    fclose(GE);

    return 0;
}
