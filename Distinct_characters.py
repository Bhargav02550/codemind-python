n=input().lower()
b=[]
for i in n:
    if i not in b and i!=' ':
        b.append(i)
for i in sorted(b):
    print(i,end='')