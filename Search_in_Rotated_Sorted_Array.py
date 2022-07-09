n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
for i in range(n):
    if a[i]==m:
        c=1
        print(i)
if c==0:
    print('-1')