n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    a[i]=a[i]*a[i]
    b.append(a[i])
b.sort()
print(*b)
    