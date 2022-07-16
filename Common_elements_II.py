m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i not in b:
        if i not in c:
            c.append(i)
for i in b:
    if i not in a:
        if i not in c:
            c.append(i)
print(*c)