s = input().lower()
s = s.split(" ")
a = s[0]
c=0
for i in a:
    count = 0
    for j in range(1,len(s)):
        if i in s[j]:
            count+=1
    if count==len(s)-1:
        c+=1
print(c)