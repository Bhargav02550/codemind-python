m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%n==0:
        c+=1
print(c)