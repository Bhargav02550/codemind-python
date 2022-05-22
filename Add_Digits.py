def da(n):
    while(n>9):
        s=0
        while(n>0):
            r=n%10
            s+=r
            n=n//10
        n=s
    return s
n=int(input())
m=da(n)
print(m)
        

        