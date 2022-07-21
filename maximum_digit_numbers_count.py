n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
    if m<len(str(i)):
        m=len(str(i))
for i in a:
    if len(str(i))==m:
        print(i,end=' ')