#include<stdio.h>
#include <stl.h>
#define NCARDS 52 /* number of cards */
#define NSUITS 4 /* number of suits */
char values[] = "23456789TJQKA";
char suits[] = "cdhs";
int rank_card(char value, char suit)
{
int i,j; /* counters */
for (i=0; i<(NCARDS/NSUITS); i++)
if (values[i]==value)
for (j=0; j<NSUITS; j++)
if (suits[j]==suit)
return( i*NSUITS + j );
printf("Warning: bad input value=%d, suit=%d\n",value,suit);
}
char suit(int card)
{
return( suits[card % NSUITS] );
}
char value(int card)
{
return( values[card/NSUITS] );
}

main()
{
queue decks[2]; /* player’s decks */
char value,suit,c; /* input characters */
int i; /* deck counter */
while (TRUE) {
    for (i=0; i<=1; i++) {
    init_queue(&decks[i]);
    while ((c = getchar()) != ’\n’) {
    if (c == EOF) return;
    if (c != ’ ’) {
    value = c;
    suit = getchar();
    enqueue(&decks[i],rank_card(value,suit));
    }
    }
    }
    war(&decks[0],&decks[1]);
    }
    }

    war(queue *a, queue *b)
    {
    int steps=0; /* step counter */
    int x,y; /* top cards */
    queue c; /* cards involved in the war */
    bool inwar; /* are we involved in a war? */
    inwar = FALSE;
    init_queue(&c);
    while ((!empty(a)) && (!empty(b) && (steps < MAXSTEPS))) {
    steps = steps + 1;
    x = dequeue(a);
    y = dequeue(b);
    enqueue(&c,x);
    enqueue(&c,y);
if (inwar) {
inwar = FALSE;
} else {
if (value(x) > value(y))
clear_queue(&c,a);
else if (value(x) < value(y))
clear_queue(&c,b);
else if (value(y) == value(x))
inwar = TRUE;
}
}
if (!empty(a) && empty(b))
printf("a wins in %d steps \n",steps);
else if (empty(a) && !empty(b))
printf("b wins in %d steps \n",steps);
else if (!empty(a) && !empty(b))
printf("game tied after %d steps, |a|=%d |b|=%d \n",
steps,a->count,b->count);
else
printf("a and b tie in %d steps \n",steps);
}
clear_queue(queue *a, queue *b)
{
while (!empty(a)) enqueue(b,dequeue(a));
}