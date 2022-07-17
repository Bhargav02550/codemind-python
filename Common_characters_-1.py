s = input().lower()
s = s.split(" ")
a = s[0]
x = ''
for i in a:
    count = 0
    for j in range(1,len(s)):
        if i in s[j]:
            count+=1
    if count==len(s)-1:
        x+=i
if len(x)==0:
    print("-1")
else:
    print(x)