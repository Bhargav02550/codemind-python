n,m,k=map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
c,ap,bp=0,0,0
while ap<n:
    while bp<m and b[bp]<a[ap]-k:
        bp+=1
    if bp<m and a[ap]-k<=b[bp] and b[bp]<=a[ap]+k:
        c+=1
        ap+=1
        bp+=1
    else:
        ap+=1
print(c)