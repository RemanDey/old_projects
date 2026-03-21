#include<stdio.h>

int main()
{
    int n,i,gcd;
    printf("Enter how many numbers you want to find Gcd : ");
    scanf("%d",&n);
    int arr[n];
    printf("\nEnter the numbers below :- \n ");
    for(i=0;i<n;i++)
    {
        printf("\nEnter Number[%d] = ",i+1);
        scanf("%d",&arr[i]);
    }
    gcd=arr[0];
    int j=1;
    while(j<n)
    {
       if(arr[j]%gcd==0)
       {
           j++;
       }
       else
       {
           gcd=arr[j]%gcd;
           i++;
       }
    }
    printf("\nGCD= %d ",gcd);
    return 0;
}