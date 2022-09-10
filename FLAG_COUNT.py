n=int(input())
w=0
r=2
for i in range(n):
    temp=w
    w=r
    r+=temp
print(w)