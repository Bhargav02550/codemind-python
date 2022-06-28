n=int(input())
a=list(map(int,input().split()))
s,c=0,0
for i in a:
    s+=i
k=s//n
for i in a:
    if i<=k:
        c+=1
print(c)