n=input().lower()
s=[]
for i in n:
    if n.count(i)==1:
        s.append(i)
        break
if len(s)==0:
    print("-1")
else:
    print(*s)