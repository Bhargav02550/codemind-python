def p(n):
    if(n==1):
        return 0;
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    return 1
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(p(i)):
        print(i)