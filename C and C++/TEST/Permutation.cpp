#include <iostream>
#include <vector>
using namespace std;
int main()
{   int input;
    int k;
    vector<int> S={};
scanf("%d",&k);
for (int i = 0; i < k; i++) // input: k sorted integers
{
    scanf("%d", &input);
    S.push_back(input);
}

for (int a = 0 ; a < k - 5; a++) // six nested loops!
for (int b = a + 1; b < k - 4; b++)
for (int c = b + 1; c < k - 3; c++)
for (int d = c + 1; d < k - 2; d++)
for (int e = d + 1; e < k - 1; e++)
for (int f = e + 1; f < k ; f++)
printf("%d %d %d %d %d %d\n",S[a],S[b],S[c],S[d],S[e],S[f]);
}