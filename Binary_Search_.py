m,n=map(int,input().split())
a=list(map(int,input().split()))
c,d=0,0
for i in a:
    if i==n:
        c=a.index(i)
        d+=1
if d==0:
    print(-1)
else:
    print(c)