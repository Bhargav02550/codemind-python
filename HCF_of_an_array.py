def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
n=int(input())
a=list(map(int,input().split()))
r=0
for i in a[1::]:
    r=gcd(r,i)
print(r)