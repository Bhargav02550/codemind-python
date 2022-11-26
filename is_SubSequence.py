s=input().lower()
a='qwertyuiopasdfghjklzxcvbnm'
b=''
for i in s:
    if i in a:
        b+=i
if b==b[::-1]:
    print("true")
else:
    print("false")