def sq(n):
    c=n*n
    return c
def rev(n):
    t=n
    s=0
    while(n):
        s=s*10+n%10
        n=n//10
    return s
n=int(input())
n1=rev(n)
n2=rev(sq(n1))
n3=sq(n)
if n2==n3:
    print(True)
else:
    print(False)
