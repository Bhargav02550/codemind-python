n=input()
n=n.split(" ")
n=('').join(n)
c=0
d=0
for i in n:
    if i==min(n):
        c+=1
    if i==max(n):
        d+=1
print(min(n),c,end=' ')
print(max(n),d)