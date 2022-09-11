n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in range(0,n):
    b.append(max(a))
    a[a.index(max(a))]=0
for i in range(0,len(b)):
    if i%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
i=0
j=0
while(i<len(c)) or (j<len(d)):
    if i<len(d):
        print(d[i],end=' ')
    if j<len(c):
        print(c[i],end=' ')
    i+=1
    j+=1