def prime_left(x):
    while x:
        fact=0
        c=2
        count=0
        while c<=x//2:
            if x%c==0:
                count+=1
            c+=1
        if count==0:
            return x
            break
        x-=1
def prime_right(x):
    while x:
        fact=0
        c=2
        count=0
        while c<=x//2:
            if x%c==0:
                count+=1
            c+=1
        if count==0:
            return x
            break
        x+=1

n = int(input())
while n:
    num = int(input())
    left = num
    right = num
    l=prime_left(left)
    r=prime_right(right)
    if r-num<num-l:
        print(r)
    else:
        print(l)
    n-=1