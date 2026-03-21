#include <stdio.h>  
#include <string.h>  
int main()  
{  
char str1[50], temp;  
int i = 0, j =0 , n;  
printf (" Enter a string to be reversed: ");  
scanf( "%s", str1);  
for(n=0; str1[n]!='\0'; n++);
j = n - 1;  

while ( i < j)   
{  
temp = str1[j];  
str1[j] = str1[i];  
str1[i] = temp;  
i++; 
j--; 
}  
printf (" The reversed string: %s", str1);  
return 0;  
} 