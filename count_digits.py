def c(n):
    return len(str(n))
n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i<0:
        k=i*-1
        print(c(k),end=' ')
    else:
        print(c(i),end=' ')