# include <stdio.h>
# include <string.h>

int main()
{   char string[30],reverse_string[30]={'\0'};
    int i,length=0,flag=1;
    printf("Enter the string or number:-");
    scanf("%s",string);

    for(i=0;string[i]!='\0';i++)
    {length++;}

    for(i=length-1;i>=0;i--)
    {reverse_string[length-i-1]=string[i];}

    for(i=0;i<length;i++)
    {if(reverse_string[i]!=string[i])
            flag=0;}

    if(flag==1)
        {printf("%s is a palindrome",string);}
    else if(flag==0)
        {printf("%s is NOT a palindrome", string);}
return 0;}
