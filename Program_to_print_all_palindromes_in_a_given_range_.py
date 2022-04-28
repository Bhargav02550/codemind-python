m=int(input())
n=int(input())
for x in range (m,n+1):
    y=x
    r=0
    while(y>0):
        r=r*10+y%10
        y=y//10
    if(x==r):
        print(x,end=' ')