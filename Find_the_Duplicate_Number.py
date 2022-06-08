n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if a[i]==a[j]:
            print(a[i])