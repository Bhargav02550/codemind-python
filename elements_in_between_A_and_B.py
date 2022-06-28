n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
e=0
for i in range(n):
    if a[i]>=c and a[i]<=d:
        e+=1
        print(a[i],end=' ')
if e==0:
    print("-1")