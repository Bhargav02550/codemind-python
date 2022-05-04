n=int(input())
e=0
o=0
while n:
    if (n%10)%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if o==0 and e>0:
    print("Even")
elif e==0 and o>0:
    print("Odd")
else:
    print("Mixed")