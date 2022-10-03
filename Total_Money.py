for _ in range(int(input())):
    d,x,p,q=map(int,input().split())
    print(((d//x)*p+(((d//x)*((d//x)-1))//2)*q)*x+(p+(d//x)*q)*(d%x))