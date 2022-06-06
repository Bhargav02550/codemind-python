n=input()
a='aeiouAEIOU'
c=0
b=[]
for i in n:
    if i in a:
        if i not in b:
            b.append(i)
print(*b)