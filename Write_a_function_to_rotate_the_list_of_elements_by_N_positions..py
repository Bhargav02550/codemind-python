n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    temp=a[0]
    a[0]=a[n-1]
    for j in range(1,n):
        d=a[j]
        a[j]=temp
        temp=d
for i in a:
    print(i,end=' ')