n=int(input())
c=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
f=[]
e=0
for i in range(n):
    if c[i]>=a and c[i]<=b:
        d.append(c[i])
for i in range(n):
    if c[i] not in d:
        e+=1
        f.append(c[i])
if e==0:
    print("-1")
else:
    print(min(f))