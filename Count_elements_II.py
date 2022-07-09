m,n=map(int,input().split())
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
c=0
for i in a:
    if i not in b:
        c+=1
for i in b:
    if i not in a:
        c+=1
print(c)