n = int(input())
b = []
for i in range(n):
    a = input()
    b.append(a)
c = b[len(b)-1]
i = c.index(' ')
x = c[i+1::]
print(x)