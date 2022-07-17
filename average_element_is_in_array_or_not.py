n=int(input())
a=list(map(int,input().split()))
k=sum(a)//n
if k in a:
    print(True)
else:
    print(False)