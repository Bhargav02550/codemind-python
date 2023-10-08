a,b=map(int,input().split())
ar=list(map(int,input().split()))
res=[]
f=0
i,j=0,a-1
while i<=j:
    m=(i+j)//2
    res.append(ar[m])
    if ar[m]==b:
        f=1
        break
    if ar[m]>b:
        j=m-1
    else:
        i=m+1
if f==1:
    print(*res)
else:
    print(*res,end=" -1")
