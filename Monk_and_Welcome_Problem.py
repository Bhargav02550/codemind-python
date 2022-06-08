n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i==j:
            print(a[i]+b[j],end=' ')