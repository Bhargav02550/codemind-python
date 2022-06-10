n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n//2,n):
    b.append(a[i])
print(*b[::-1],end=' ')
for i in range(0,n//2):
    print(a[i],end=' ')