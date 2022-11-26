for i in range(int(input())):
    N,R,K,C=map(int,input().split())
    l=1
    h=N
    while(l<=h):
        m=(l+h)//2
        r=N-m
        n=R+r*K
        if(m*C<=n):
            l=m+1
        else:
            h=m-1
    print(h)