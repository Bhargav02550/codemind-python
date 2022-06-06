n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if i%2==0:
        s+=a[i]
    else:
        s1+=a[i]
z=abs(s-s1)
if(z==0):
    print("YES")
else:
    print("NO")