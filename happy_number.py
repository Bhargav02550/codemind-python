def s(n):
    r=s=0
    while(n>0):
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
n=int(input())
res=n
while(res!=1 and res!=4):
    res=s(res)
if(res==1):
    print(True)
elif(res==4):
    print(False)
