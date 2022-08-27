n = int(input())
arr = list(map(int,input().split()))
if n%2:
    f = arr[0:(n//2)+1]
    l = arr[n-1:n//2:-1]
else:
    f = arr[0:(n//2)]
    l = arr[n-1:n//2-1:-1]
if n%2:
    l.append(0)
for i in range(len(f)):
    print(f[i],l[i],end=" ")