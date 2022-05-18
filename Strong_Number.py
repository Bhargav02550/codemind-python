def f(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        k=1
        for i in range (1,n+1):
            k=k*i
        return k
m=int(input())
t=m
s=0
r=0
while(m):
    r=m%10
    s=s+f(r)
    m=m//10
if(s==t):
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")
    
            
