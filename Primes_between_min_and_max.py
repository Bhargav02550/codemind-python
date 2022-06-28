def p(n):
    if n==1:
        return 0
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
m=a.index(max(a))
m1=a.index(min(a))
if m<m1:
    m,m1=m1,m
for i in range(m1,m+1):
    if p(a[i]):
        c+=1
print(c)