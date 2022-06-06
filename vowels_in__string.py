n=input()
a='aeiouAEIOU'
b=[]
c=0
for i in n:
    if i in a:
        if i not in b:
            b.append(i)
print(*b)