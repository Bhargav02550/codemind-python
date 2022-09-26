n=int(input())
a=list(map(int,input().split()))
c,s=a[0],a[0]
for i in range(1,n):
    c=max(a[i],c+a[i])
    s=max(s,c)
print(s)