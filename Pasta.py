n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
se = set(b)
if len(se)==len(b):
    for i in b:
        if i in a:
            c+=1
    if c==len(b):
        print("Yes")
    else:
        print("No")
else:
    print("No")