n=int(input())
a=list(map(int,input().split()))
b,c=[],[]
for i in range(int(n/2)):
    b.append(a[i])
    b.append(a[i+int(n/2)])
print(*b)