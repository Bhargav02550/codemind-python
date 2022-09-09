n=int(input())
while(n):
    c=int(input())
    s=input()
    b=''
    for i in s:
        if s.count(i)==1:
            b+=i
            break
    if len(b)==0:
        print("-1")
    else:
        print(b)
    n-=1