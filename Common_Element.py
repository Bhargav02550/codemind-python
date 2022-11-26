for i in range(int(input())):
    a,b,c=map(int,input().split())
    a1=list(map(int,input().split()))
    b1=list(map(int,input().split()))
    c1=list(map(int,input().split()))
    d=[]
    for i in a1:
        if i in b1 and i in c1 and i not in d:
            d.append(i)
    for i in d:
        print(i,end=" ")
    print()