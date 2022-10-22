n=int(input())
l=list(map(int,input().split()))
ans='NO'
for i in range(1<<n):
        sub=0
        for j in range(n):
                if i&1<<j:
                        sub+=l[j]
                else:
                        sub-=l[j]
        if sub%360==0:
                ans='YES'
print(ans)