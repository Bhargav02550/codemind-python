m=input()
n=input()
c=0
m2=m.lower()
n2=n.lower()
m1=m2.split(' ')
n1=n2.split(' ')
for i in m1:
    for j in n1:
        if(i==j):
            c+=1
print(c)