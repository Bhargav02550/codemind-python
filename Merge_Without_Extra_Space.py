for _ in range(int(input())):
    m,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    print(*sorted(c))