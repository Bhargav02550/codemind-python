n=input().lower()
c=0
for i in n:
    if n.count(i)==1 and i!=' ':
        c+=1
print(c)