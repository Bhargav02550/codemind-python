def sep(n):
    s=0
    while(n!=0):
       s=s+n%10
       n=n//10
    return s
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=sep(i)
print(s)
    