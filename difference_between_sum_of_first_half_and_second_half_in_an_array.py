n=int(input())
a=list(map(int,input().split()))
s,s1=0,0
for i in range(0,int(n/2)):
    s+=a[i]
for i in range(int(n/2),n):
    s1+=a[i]
print(abs(s-s1))