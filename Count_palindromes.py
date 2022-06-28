def p(n):
    if str(n)[::-1]==str(n):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if p(i):
        c+=1
print(c)