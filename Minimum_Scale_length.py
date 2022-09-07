n = int(input())
arr = list(map(int,input().split()))
min=min(arr)
count = 0
while min:
    count = 0
    for j in range(0,n):
        if arr[j]%min==0:
            count+=1
    if count==n:
        print(min)
        break
    min-=1