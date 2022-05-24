import math
def p(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
m=int(input())
n=int(input())
o=m+n
for i in range(1,1000000):
    if(p(o+i)):
        print(i)
        break