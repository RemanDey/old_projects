#include <iostream>
# include<vector>
# include<algorithm>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    int n; cin>>n;
    while(n--){
        int x,y; cin>>x>>y;
        if(x==a||y==b)cout<<"divisa\n";
        else if(x>a&&y>b)cout<<"NE\n";
        else if(x<a&&y>b)cout<<"NW\n";
        else if(x<a&&y<b)cout<<"SW\n";
        else cout<<"SE\n";
    }
}