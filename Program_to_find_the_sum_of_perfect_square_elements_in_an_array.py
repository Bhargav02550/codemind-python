def ps(n):
    for i in range(1,n+1):
        if n==i*i:
            return 1
    return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if ps(i):
        c+=i
print(c)