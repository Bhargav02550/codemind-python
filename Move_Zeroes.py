def arr(a,n):
    c=0
    for i in range(n):
        if a[i]!=0:
            a[c]=a[i]
            c+=1
    while c<n:
        a[c]=0
        c+=1
n=int(input())
a=list(map(int,input().split()))
arr(a,n)
print(*a)
