for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    for i in b:
        if i not in c:
            c.append(i)
    if len(c)+1>n:
        print("YES")
    else:
        print("NO")
