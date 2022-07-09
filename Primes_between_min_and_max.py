def p(n):
    if n==1:
        return 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
mi=a.index(min(a))
ma=a.index(max(a))
if mi<ma:
    for i in range(mi,ma+1):
        if p(a[i]):
            c+=1
    print(c)
else:
    for i in range(ma,mi+1):
        if p(a[i]):
            c+=1
    print(c)