n=int(input())
for i in range(n,1,-1):
    for j in range(n,0,-1):
        if j>i:
            print(j,end=" ")
        else:
            print(i,end=" ")
    for j in range(2,n+1):
        if j>i:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j>i):
            print(j,end=" ")
        else:
            print(i,end=" ")
    for j in range(2,n+1):
        if(j>i):
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()