#include<bits/stdc++.h>
using namespace std;
int delrow[8]={-2,-2,-1,-1,1,1,2,2};
int delcol[8]={-1,1,-2,2,-2,2,-1,1};
int bfs(int n,int m,int row,int col)
{
    long long ans=n*m;
    ans--;
    for(int i=0;i<8;i++)
    {
        int nrow=row+delrow[i];
        int ncol=col+delcol[i];
        if(nrow>=0 and nrow<n and ncol>=0 and ncol<m)
        {
            ans--;
        }
    }
    return ans;
}
int main()
{
    int n,m;
    cin>>n>>m;
    int ans=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            int x=bfs(n,m,i,j);
            ans+=x;
        }
    }
    cout<<ans;
}
