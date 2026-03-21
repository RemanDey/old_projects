#include<iostream>

using namespace std;
int main()
{
    int n;cin>>n;
    while(n--)
    {
        long long int a;cin>>a;
        a=(a*567/9+7492)*235/47-498;
        a=(a/10)%10;
        if(a<0)a*=-1;
        cout<<a<<endl;
    }


}