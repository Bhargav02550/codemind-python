n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in range(0,n):
    if a[i]<x or a[i]>y:
        s+=a[i]
print(s)