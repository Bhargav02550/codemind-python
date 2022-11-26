for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.append(k)
    arr.sort()
    print(arr.index(k))