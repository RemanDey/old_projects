#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin>>t;
    while(t--){
        int n;cin>>n;
        int m; cin>>m;
        int a;
        a=m;
        int flag=0;
        vector<int> v;
        while(m>0){
            int x;cin>>x;
            v.push_back(x);
            m--;
        }
        for(int i=0;i<a-1;i++){
            if(v[i]>=v[i+1]){
                flag=1;   
                break;
            }     
            }
        if(flag==0){
            cout<<n-v.back()+1<<endl;     
        }
        else if(flag==1){
            cout<<1<<endl;
        }
    }
}

