n=int(input())
while(n):
    a,b=map(int,input().split())
    c=max(a,b)
    ans=-1
    for i in range(0,c+1):
        if (i*i)%b==a:
            ans=i
            break
    print(ans)
    n-=1