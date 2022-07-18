n = int(input())
f,s = 0,1
ne = f+s
while ne<=n:
    f=s
    s=ne
    ne=f+s
if n-s<ne-n:
    print(s)
elif n-s>ne-n:
    print(ne)
else:
    print(s,ne)