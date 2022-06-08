def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
n=int(input())
a=list(map(int,input().split()))
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm,i)
print(lcm)