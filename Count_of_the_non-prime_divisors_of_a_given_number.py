def p(n):
    if(n==1):
        return 1
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 1
    else:
        return 0
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(p(i)):
            c+=1
print(c)