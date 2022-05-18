m,n=input().split()
m=int(m)
n=int(n)
if n+1==m or m+1==n:
    print("Yes")
elif m==10 and n==1 or m==1 and n==10:
    print("Yes")
else:
    print("No")