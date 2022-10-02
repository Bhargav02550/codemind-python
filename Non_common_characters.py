n=input().lower()
m=input().lower()
s=''
for i in n:
    if i not in m and i not in s:
        s+=i
for i in m:
    if i not in n and i not in s:
        s+=i
s=s.replace(" ","")
print(len(s))