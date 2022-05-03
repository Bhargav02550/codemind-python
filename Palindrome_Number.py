def p(n):
    r=0
    while(n):
        m=n%10
        r=r*10+m
        n=n//10
    return r
n=int(input())
for i in range(n):
    m=int(input())
    if(p(m)==m):
        print(True)
    else:
        print(False)

        