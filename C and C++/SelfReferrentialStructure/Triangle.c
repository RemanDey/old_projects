#include <stdio.h>
void main()
{
    int qwerty;
    struct point
    {
        int x;int y; struct point *next;
    }p1,p2,p3;

p1.x=2; p1.y=2;
p2.x=5; p2.y=5;
p3.x=8; p3.y=4;
p1.next=&p2;
p2.next=&p3;
p3.next=NULL;
printf("\n A program implementing A self referential structure...");
printf("\n1st point: (%d,%d)",p1.x,p1.y);
printf("\n2nd point: (%d,%d)",p1.next->x,p1.next->y);
printf("\n3rd point: (%d,%d)",p1.next->next->x,p1.next->next->y);
scanf("%d",&qwerty);
}