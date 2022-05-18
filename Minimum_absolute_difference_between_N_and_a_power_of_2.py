import math
n=int(input())
l=pow(2,int(math.log2(n)))
r=l*2
if(n-l>r-n):
    print(abs(r-n))
else:
    print(abs(n-l))
