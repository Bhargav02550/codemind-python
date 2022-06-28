n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
e=0
b=[]
for i in range(n):
    if a[i]>=c and a[i]<=d:
        e+=a[i]
print(e)