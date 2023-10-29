n = int(input())
a = list(map(int, input().split()))
if a == sorted(a):
    print("YES")
    print("1 1")
else:
    first_dec = -1
    last_dec = -1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            first_dec = i
            break
    for i in range(n - 1, 0, -1):
        if a[i] < a[i - 1]:
            last_dec = i
            break
    a[first_dec:last_dec + 1] = reversed(a[first_dec:last_dec + 1])
    if a == sorted(a):
        print("YES")
        print(first_dec + 1, last_dec + 1)
    else:
        print("NO")
