n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in a:
    if i<x or i>y:
        c+=1
        print(i,end=' ')
if c==0:
    print("-1")