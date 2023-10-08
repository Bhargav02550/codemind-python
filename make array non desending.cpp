#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    stack<pair<int,int>> st;
    int maxi=0;
    st.push({arr[n-1],0});
    for(int i=n-2;i>=0;i--){
        int steps=0;
        while(!st.empty() && st.top().first<arr[i]){
            steps=max(steps+1,st.top().second);
            st.pop();
        }
        maxi=max(maxi,steps);
        st.push({arr[i],steps});
    }
    cout<<maxi;
}
