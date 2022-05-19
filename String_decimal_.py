n=int(input())
for i in range(1,n+1):
    m=input()
    l=len(m)
    c=0
    for i in (m):
        if(i>=str(0) and i<=str(9)):
            c=c+1
    if(c==l):
        print(True)
    else:
        print(False)