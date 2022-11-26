for _ in range(int(input())):
    n,m = map(int,input().split())
    r = []
    for i in range(n):
        a = list(map(int,input().split()))
        r.extend(a)
    r.sort()
    print(r[len(r)//2])