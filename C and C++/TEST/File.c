#include<stdio.h>
void main()
{
    FILE *fp;
    fp=fopen("we.txt","a");
    fputs("Dodo",fp);
    fclose(fp);
}