def p(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
c=0
for i in range(2,n):
    if(n%i==0):
        if(p(i)):
            c+=1
            print(i,end=' ')
if(c==0):
    print("-1")