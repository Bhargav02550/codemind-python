m,n=map(int,input().split())
a=list(map(int,input().split()))
c,d=0,0
for i in range(m):
    if a[i]==n:
        c=i
        d+=1
if d==0:
    print('-1')
else:
    print(c)