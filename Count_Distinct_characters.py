n=input().lower()
s=[]
for i in n:
    if i not in s and i!=' ':
        s.append(i)
print(len(s))