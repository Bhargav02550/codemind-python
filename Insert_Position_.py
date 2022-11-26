for i in range(int(input())):
    m,n=map(int,input().split())
    a=list(map(int,input().split()))
    a.append(n)
    a.sort()
    for i in range(m,-1,-1):
        if a[i]==n:
            print(i)
            break