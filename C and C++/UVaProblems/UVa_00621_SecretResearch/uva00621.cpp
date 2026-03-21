#include <iostream>
#include <string>
using namespace std;
int main(){
    int n;cin>>n;
    while(n--){
        string s; cin>>s;
        if(s=="1"||s=="4"||s=="78") cout<<"+\n";
        else if(s.size()>=2&&s[s.size()-1]=='5'&&s[s.size()-2]=='3') cout<<"-\n";
        else if(s.size()>=3&&s[0]=='9'&&s[-1]=='4')cout<<"*\n";
        else if(s.size()>=4&&s[0]=='1'&&s[1]=='9'&&s[2]=='0')cout<<"?\n";
        else cout<<"?\n";
    }
    return 0;
}