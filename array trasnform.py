n = int(input())
s = sorted(map(int, input().split()))
p = f = 0
for i in s:
    if i > 1 and i > p:
        f = 1
        break
    p += i
print("YES" if not f else "NO")
