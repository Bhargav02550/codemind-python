def p(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r
n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(p(i),end=" ")