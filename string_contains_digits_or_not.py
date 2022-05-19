n=int(input())
for i in range(1,n+1):
    m=input()
    c=0
    for i in (m):
        if(i>=str(0) and i<=str(9)):
            c+=1
    if(c==0):
        print('No')
    else:
        print('Yes')