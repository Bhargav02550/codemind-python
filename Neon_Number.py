n=int(input())
s=n*n
p=0
while s>0:
    r=s%10
    p+=r
    s=s//10
if(p==n):
    print("Neon Number")
else:
    print("Not Neon Number")

    