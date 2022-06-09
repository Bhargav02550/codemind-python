n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
c1=0
for i in range(n):
    for j in range(i):
        if a[i]==a[j]:
            b.append(a[j])
for i in range(n):
    if a[i] not in b:
        c1+=1
        c.append(a[i])
if c1==0:
    print("-1")
else:
    print(max(c))