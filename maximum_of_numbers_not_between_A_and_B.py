n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
d,f=[],[]
for i in a:
    if i>=x and i<=y:
       d.append(i)
for i in a:
    if i not in d:
        f.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(max(f))