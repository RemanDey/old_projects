#include <stdio.h>
int main()
{
    extern int a, b, c;
    printf("Enter the numbers: "); scanf("%d %d %d",&a,&b,&c);
   
    if (a <= b && a <= c)
        printf("%d is the smallest",a);
    else if (b <= a && b <= c)
        printf("%d is the smallest",b);
    else
        printf("%d is the smallest",c);
 
    return 0;
}