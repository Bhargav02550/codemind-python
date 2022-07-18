n=int(input())
a=[]
b=[]
for j in range(2):
    for l in range(n):
        m=list(map(int,input().split()))
        if j==0:
            for h in m:
                a.append(h)
        if j==1:
            for g in m:
                b.append(g)
for k in range(n*n):
    if k%n==(n-1):
        print(abs(b[k]-a[k]))
    else:
        print(abs(b[k]-a[k]),end=' ')