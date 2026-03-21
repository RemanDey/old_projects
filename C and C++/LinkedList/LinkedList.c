#include<stdio.h>
typedef struct record
    {
        int value;
        struct record *next;
    }NODE;
NODE *start=NULL;
void append(int data);
void display();
void main()
{   
    int request, data, exit;

    do{
        printf("\nEnter <1> to enter data,<2> to display, <0>to exit: ");
        scanf("%d",&request);
        printf("\n--------------------------------------------------------------------\n");
        
        if(request==1)
        {
        printf("\nEnter Data:");
        scanf("%d",&data);
        append(data);
        }
        else if(request==2)
        display();
    } while(request!=0);
    display();
    scanf("%d",exit);
    
}
void append(int data)
{
    NODE *temp, *curr;
    curr=start;
    temp=(NODE*)malloc(sizeof(NODE));
    temp->next= NULL;
    temp->value=data;
    if(start==NULL)
    {
        start=temp;
    }
    else
    {
        curr=start;
        while(curr->next!=NULL)
        {
            curr=curr->next;

        }
        curr->next=temp;

    }
}
void display()
{
    int count=0;
    NODE *curr=start;
    printf("\nCurrent List:");
    while(curr!=NULL)
        {
            printf("DATA[%d]=%d\n",++count,curr->value);
            curr=curr->next;
        }
    
}