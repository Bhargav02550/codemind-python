n=input()
m=input()
a=[]
b=[]
for i in n:
    if i=='#':
        a.pop()
    else:
        a.append(i)
for i in m:
    if i=='#':
        b.pop()
    else:
        b.append(i)
if a==b:
    print("True")
else:
    print("False")