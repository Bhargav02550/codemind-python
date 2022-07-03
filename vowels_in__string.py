n=input()
a='aeiouAEIOU'
c=0
b=[]
for i in n:
    if i in a:
        if i not in b:
            b.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(*b)