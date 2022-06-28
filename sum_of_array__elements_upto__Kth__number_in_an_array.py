n=int(input())
a=list(map(int,input().split()))
m=int(input())
s=0
for i in range(n):
    if a[i]==m:
        k=i
for j in range(0,k+1):
    s+=a[j]
print(s)