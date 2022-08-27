s = input().lower()
s = s.replace(" ","")
x = 0
for i in s:
    if s.count(i)==1:
        x+=1
print(x)