n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j] and a[i]!=0 and a[j]!=0 and i!=j:
            c+=1
            a[i]=0
            a[j]=0
print(c)