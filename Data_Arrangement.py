n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i<0:
        print(i,end=" ")
for i in a:
    if i>-1:
        print(i,end=" ")