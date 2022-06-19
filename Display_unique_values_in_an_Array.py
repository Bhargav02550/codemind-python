n=int(input())
a=list(map(int,input().split()))
b=[]
d=[]
c=0
for i in range(n):
    for j in range(i):
        if a[i]==a[j]:
            if a[i] not in b:
                b.append(a[i])
for i in range(n):
    if a[i] not in b:
        c+=1
        d.append(a[i])
if c==0:
    print('-1')
else:
    print(*d)