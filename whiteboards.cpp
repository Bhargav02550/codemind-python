#include<bits/stdc++.h>
using namespace std;
 int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n,m;
        cin>>n>>m;
        long long int s=0;
        priority_queue<long long int,vector<long long int>,greater<long long int>>pq;
        long long int a[n];
        for(long long int i=0;i<n;i++)
        {
            long long int temp;
            cin>>temp;
            pq.push(temp);
        }
        long long int b[n];
        for(long long int i=0;i<m;i++)
        {
            int temp;
            cin>>temp;
            pq.pop();
            pq.push(temp);
        }
        while(!pq.empty())
        {
            s+=pq.top();
            pq.pop();
        }
        cout<<s<<endl;

    }
}
