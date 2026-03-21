#include<stdio.h>
#include<conio.h>
int findSmallest(int arr[], int n)
{   int i=0, small;
    small=arr[i];
    while(i<n)
    {
        if(small>arr[i])
            small = arr[i];
        i++;
    }
    return small;
}
int main()
{   int arr[50], small, i, size;
    printf("Enter Array Size: ");scanf("%d", &size);
    printf("\nEnter %d Array Elements: ", size);
    for(i=0; i<size; i++)
        scanf("%d", &arr[i]);
    small=findSmallest(arr, size);
    printf("\nSmallest Number = %d", small);
    return 0;
}
