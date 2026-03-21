#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>

int main(){
    int t,n; cin>>t;
    vector <int> v={};

    while(t--){
        cin>>n;
        v.push_back(n);
    }
    sort(v.begin(),v.end());
    cout<<(v.back()-v.front())*2<<endl;
    return 0;
}