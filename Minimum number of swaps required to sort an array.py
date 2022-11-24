n=int(input())
a=list(map(int,input().split()))
x=a.copy()
a.sort()
c=0
for i in range(n):
    if a[i]!=x[i]:
        c+=1
        index=a.index(x[i])
        a[i],a[index]=a[index],a[i]
print(c)
