n=int(input())
for i in range(n):
    m=int(input())
    s=0
    k=list(map(int,input().split()))
    for i in k:
        s+=i
    a=m*(m+1)//2
    print(abs(a-s))