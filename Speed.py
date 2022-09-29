n=int(input())
while(n):
    a=int(input())
    c=1
    li=list(map(int,input().split()))
    for i in range(a-1):
        if(li[i]>li[i+1]):
            c+=1
    print(c)
    n-=1;