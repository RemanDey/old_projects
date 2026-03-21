#include<stdio.h>
int main()
{
    FILE *out;
    out=fopen("text.txt","w");
    fprintf(out,"I am Reman Dey");
    fclose(out);
}