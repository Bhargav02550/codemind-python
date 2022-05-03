def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        k=1
        for i in range (1,n+1):
            k=k*i
        return k
n=int(input())
for i in range(n):
    m=int(input())
    print(f(m))