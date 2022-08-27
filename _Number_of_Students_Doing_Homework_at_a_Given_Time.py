n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    for j in range(m):
        if a[i]<=q and b[j]>=q and i==j:
            c+=1
print(c)