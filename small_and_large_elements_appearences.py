n=input()
a=' '
m=set(n)
b=[]
c,c1=0,0
for i in m:
    if i not in a:
        b.append(i)
for i in n:
    if min(b)==i:
        c+=1
print(min(b),c,end=' ')
for i in n:
    if max(b)==i:
        c1+=1
print(max(b),c1)