n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if a.count(i)==i:
        c+=1
        b.append(i)
if c==0:
    print("-1")
else:
    print(min(b),max(b))