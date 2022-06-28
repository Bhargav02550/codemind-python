n=int(input())
a=list(map(int,input().split()))
e,d=[],[]
for i in range(n):
    if a[i]%2==0:
        e.append(a[i])
    else:
        d.append(a[i])
f,g=0,0
while f<len(e) or g<len(d):
    if g<len(d):
        print(d[g],end=" ")
        g+=1
    if f<len(e):
        print(e[f],end=" ")
        f+=1
if n%2!=0:
    print('0')