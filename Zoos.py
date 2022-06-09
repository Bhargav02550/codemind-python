n=input()
c=0
c1=0
for i in n:
    if i=='z':
        c+=1
    if i=='o':
        c1+=0.5
if(c==c1):
    print("Yes")
else:
    print("No")