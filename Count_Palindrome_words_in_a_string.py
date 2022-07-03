def p(n):
    if n[::-1]==n:
        return 1
    else:
        return 0
n=input().lower().split()
c=0
for i in n:
    if p(i):
        c+=1
print(c)