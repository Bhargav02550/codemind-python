n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=[]
c=0
for i in a:
    if a.count(i)==m:
        c+=1
        b.append(i)
if c!=0:
    print(*set(b))
else:
    print("-1")