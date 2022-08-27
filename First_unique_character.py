s = input().lower()
x = 0
for i in s:
    if s.count(i)==1:
        print(i)
        x = 1
        break
if x==0:
    print("-1")