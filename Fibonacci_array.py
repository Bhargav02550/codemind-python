n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(2,n):
    if a[i]==a[i-1]+a[i-2]:
        c+=1
    else:
        d=1
        break
if c!=0 and d==0:
    print("yes")
else:
    print("no")