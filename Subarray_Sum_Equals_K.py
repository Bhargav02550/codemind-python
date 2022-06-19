n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i,n):
        if (sum(a[i:j+1])==k):
            c+=1
print(c)