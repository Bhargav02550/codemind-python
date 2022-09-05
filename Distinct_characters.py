n=input().lower()
s=[]
for i in n:
    if n.count(i)==1 and i!=' ':
        s.append(i)
for i in sorted(s):
    print(i,end='')