a=int(input(''))

b=list(map(int,input().split()))

c=list(map(int,input().split()))

if b.count(-1)==c.count(-1):
    print('Infinite')
elif c.count(-1)==2:
    print(max(0,sum(b)-sum(c)-1))
elif b.count(-1)==2:
    print(max(0,sum(c)-sum(b)-1))
elif b.count(-1) == 1:
    if sum(b) <= sum(c):
        print(1)
    else:
        print(0)
else:
    if sum(c) <= sum(b):
        print(1)
    else:
        print(0)