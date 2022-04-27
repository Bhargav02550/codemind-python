n=int(input())
s=n*n
su=0
while s>0:
    r=s%10
    su+=r
    s=s//10
if su==n:
    print("Neon Number")
else:
    print("Not Neon Number")