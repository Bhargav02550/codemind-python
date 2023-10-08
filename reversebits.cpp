#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ll n;
    cin>>n;
    vector<int>v(32,0);
    for (int i=31; i>=0; i--){
        if (1&(n>>i))v[i]++;
    }
    ll res=0;
    ll one = 1;
    for (int i=0; i<32; i++){
        if (v[i]){
            res+=(one<<(31-i));
        }
    }
    cout<<res;
}
