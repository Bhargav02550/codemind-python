n=int(input())
s1=s2=0
j=n-1
for i in range(n):
    a=list(map(int,input().split()))
    s1+=a[i]
    s2+=a[j]
    j-=1
print("Principal Diagonal:%d"%s1)
print("Secondary Diagonal:%d"%s2)