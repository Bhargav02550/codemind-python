for _ in range(int(input())):
    n,m,o = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    z = []
    for i in range(n):
        if a[i] in b and a[i] in c and a[i] not in z:
            z.append(a[i])
    if len(z)==0:
        print(-1)
    else:
        for i in range(len(z)):
            print(z[i],end=" ")
        print()