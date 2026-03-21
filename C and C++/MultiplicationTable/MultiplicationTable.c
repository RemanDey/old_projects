#include <stdio.h>
int main() {
  int number, i, range;
  printf("Enter an integer: ");
  scanf("%d", &number);

  do{
    printf("Enter the range: ");
    scanf("%d", &range);
  } 
  while (range <= 0);
  printf("Multiplication table of %d till range %d: \n", number, range);
  for (i = 1; i <= range; ++i) {
    printf("%d * %d = %d \n", number, i, number * i);
  }
  return 0;
}