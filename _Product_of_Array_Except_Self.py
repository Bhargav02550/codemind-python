n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    p=1
    for j in range(0,n):
        if i!=j:
            p*=a[j]
    print(p ,end=' ')