def pl(n):
    s=0
    t=n
    while(n):
        s=s*10+n%10
        n=n//10
    if(t==s):
        return 1
    else:
        return 0
n=int(input())
d=0
d1=0
for i in range(n-1,1,-1):
    if(pl(i)):
        d+=i
        break
for i in range(n+1,10000000):
    if(pl(i)):
        d1=i
        break
if (n-d==d1-n):
    print(d,d1)
else:
    print(d)
