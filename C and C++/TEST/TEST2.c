#include<stdio.h>
#include<stdlib.h>
typedef struct node_s
{
    int Roll;
    int Marks;
    struct node_s *next;

}node;
node *start=NULL;
void push(int Roll,int Marks)
{   node *temp;
    temp=(node*)malloc(sizeof(node));
    temp->Roll=Roll;
    temp->Marks=Marks;
    temp->next=NULL;
    if(start==NULL)
{
    start=temp;
}
    else{
        temp->next=start;
        start=temp;
    }


}
void pop()
{
    node *temp;
    temp=start;
    if(temp==NULL)
    {
        printf("\n !!Stack UnderFlow!!");
    }else{
    printf("Popped Data:\tRoll no.:%d.....Marks:%d",temp->Roll,temp->Marks);
    start=start->next;
    free(temp);
    }
}
void display(node *head)
{   FILE *output;
    output=fopen("Result.txt","w");

    if(head==NULL)
    {
        fprintf(output,"\n");
        fclose(output);

    }
    else{
        fprintf(output,"\nRoll no:%d.....Marks:%d",head->Roll,head->Marks);
        display(head->next);
    }
}
int main()
{
    int choice, Roll, Marks;
    do{
        printf("\nEnter Choice([1]->Push;[2]->Pop;[3]->Display Results;[0]To Exit):");scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            printf("\nEnter Roll and Marks:");scanf("%d %d",&Roll,&Marks);
            push(Roll,Marks);
            break;
            case 2:
            pop();
            break;
            case 3:
            display(start);
            break;

        }

    }while(choice!=0);
    return 0;
}