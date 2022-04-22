n=int(input())
m=n
r=0
s=0
while n>0:
    r=n%10
    s+=r
    n=n//10
if(m%s==0):
    print("True")
else:
    print("False")