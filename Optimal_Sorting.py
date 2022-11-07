for _ in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in range(1,n):
        if a[i-1]>a[i]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(a)-min(a))