s = input().lower()
x = 0
for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
        x = 1
        break
if x==0:
    print("-1")