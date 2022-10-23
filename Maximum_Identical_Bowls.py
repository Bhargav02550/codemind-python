n=int(input())
a=list(map(int,input().split()))
s=sum(a)
for i in range(n,-1,-1):
    if(s%i)==0:
        print(i)
        break
else:
    print(1)