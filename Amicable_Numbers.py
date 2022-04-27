n=int(input())
m=int(input())
s=0
s1=0
for x in range (1,n):
    if n%x==0:
        s=s+x
for y in range (1,m):
    if m%y==0:
        s1=s1+y
if s==m and s1==n:
    print("Amicable")
else:
    print("Not Amicable")