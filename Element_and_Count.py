n = int(input())
arr = list(map(int,input().split()))
se = []
for i in arr:
    if i not in se:
        se.append(i)
for i in se:
    print(i,arr.count(i),end=" ")