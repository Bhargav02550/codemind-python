n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1):
    if(a[i+1]>a[i]):
        s+=a[i+1]-a[i]
print(s)