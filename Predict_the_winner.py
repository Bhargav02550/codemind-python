n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==0:
        c+=a[i]
    else:
        d+=a[i]
if abs(c-d)%4==0:
    print('X')
else:
    print('Y')