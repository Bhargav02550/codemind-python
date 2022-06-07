n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(int(n/2)):
    s+=a[i]
for i in range(int(n/2),n):
    s1+=a[i]
print(abs(s-s1))