n=int(input())
a=list(map(int,input().split()))
for i in sorted(a):
    if a.count(i)==1:
        print(i,end=' ')