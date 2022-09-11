n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
for k in range(1,n+1):
    for i in range(n):
        if k==a[i]:
            break
    else:
        print(k)
        break