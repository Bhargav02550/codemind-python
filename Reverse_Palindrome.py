def p(n):
    return (re(n) == n)
def re(n):
    s=0
    while(n>0):
        s=s*10+n%10
        n=n//10
    return s
n=int(input())
r=0
while(n!=0):
    r=re(n)
    n=n+r
    if(p(n)):
        print(n)
        break
