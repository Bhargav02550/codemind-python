n=int(input())
c=0
for x in range (1,n+1):
    if n%x==0:
        c=c+1
if c==2:
    print("prime")
else:
    print("not a prime")