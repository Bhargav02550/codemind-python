s = list(map(str,input().split()))
s = s[len(s)-1]
n = min(s)
if s.count(n.lower())!=0:
    print(n.lower())
else:
    print(n)