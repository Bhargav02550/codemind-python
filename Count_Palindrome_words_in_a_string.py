def p(n):
    if n.lower()==n.lower()[::-1]:
        return True
n=input()
c=0
w=n.split(' ')
for i in w:
    if(p(i)):
        c+=1
print(c)
