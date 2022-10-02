for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(0,n):
                if(a[i]+a[j]==a[k] and k!=j):
                    c+=1
    if(c==0):
        print("-1")
    else:
        print(c)