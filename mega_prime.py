def p(n):
    if n==1:
        return 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
c,d=0,0
if p(n):
    while(n):
        if p(n%10):
            c+=1
        d+=1
        n=n//10
    if c==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")