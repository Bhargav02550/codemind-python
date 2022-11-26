for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c = -1
    for i in range(n):
        if arr[i]==i:
            print(i)
            c = 1
            break
    for i in range(-1,-1-n,-1):
        if arr[i]==i:
            print(i)
            c=1
            break
    if c==-1:
        print(c)