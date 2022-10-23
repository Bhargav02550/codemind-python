m=int(input())
for i in range(m):
    n=int(input())
    for i in range(n,0,-1):
        if(i&(i-1)==0):
            print(i)
            break