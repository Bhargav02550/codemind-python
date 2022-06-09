n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
m=int(input())
c=0
for i in b:
    if i>m:
        c+=2
    else:
        c+=1
print(c)