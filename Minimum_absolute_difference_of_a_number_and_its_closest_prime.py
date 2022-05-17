import math
def p(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
d2=0
d1=0
for i in range(n,10000000,+1):
    if(p(i)):
        d2=i
        break
for i in range(n,1,-1):
    if(p(i)):
        d1=i
        break
if(n-d2 < d1-n):
    print(abs(n-d1))
else:
    print(abs(d2-n))
    
    