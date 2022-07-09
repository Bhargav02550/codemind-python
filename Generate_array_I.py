n=int(input())
a=list(map(int,input().split()))
res = []
for i in range(0,n,2):
    while a[i+1]:
        res.append(a[i])
        a[i+1]-=1
print(*res)