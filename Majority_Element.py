n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if a[j]==a[i] and i!=j:
            c+=1
    if c>=n//2:
        print(a[i])
        break