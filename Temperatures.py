n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n-1):
    c = 0
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            print(j-i,end=" ")
            c=1
            break
    if c==0:
        print(c,end=" ")
print("0")