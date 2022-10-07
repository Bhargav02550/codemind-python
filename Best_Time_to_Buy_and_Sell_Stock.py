n=int(input())
a=list(map(int,input().split()))
d,m=0,0
for i in range(0,n):
    for j in range(i+1,n):
        d=a[j]-a[i]
        if(d>m):
            m=d
print(m)