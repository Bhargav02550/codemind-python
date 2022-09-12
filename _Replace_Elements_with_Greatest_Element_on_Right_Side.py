n=int(input())
a=list(map(int,input().split()))
mx=-1
for i in range(n-1,-1,-1):
    a[i],mx=mx,max(mx,a[i])
print(*a)