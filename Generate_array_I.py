n=int(input())
arr=list(map(int,input().split()))
res = []
for i in range(0,n,2):
    while arr[i+1]:
        res.append(arr[i])
        arr[i+1]-=1
print(*res)