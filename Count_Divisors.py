m,n,o=map(int,input().split())
c=0
for i in range (m,n+1):
    if(i%o==0):
        c=c+1
print(c)