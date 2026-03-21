#include<stdio.h>
int main()
{
	char a[20],*p;
	int c=0,i;
	p=a;
	printf("\nEnter a string:");
	gets(a);
	for(i=0;*(p+i)!='\0';i++)
	{
	if(*(p+i)>='a' && *(p+i)<='z')   
	   *(p+i)=*(p+i)-32;
	else if(*(p+i)>='A' && *(p+i)<='Z')
	   *(p+i)=*(p+i)+32;
	}
	printf("The Appended String is: %s",p);
	return 0;
}
