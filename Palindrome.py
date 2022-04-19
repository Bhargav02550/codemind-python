n=int(input())
r=0
k=n
while n>0:
    h=n%10
    r=r*10+h
    n=n//10
if k==r:
    print("True")
else:
    print("False")