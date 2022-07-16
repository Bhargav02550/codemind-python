n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
for i in set(a):
    if a.count(i)==m:
        c+=1
        print(i,end=' ')
if c==0:
    print("-1")