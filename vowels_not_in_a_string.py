n=input()
a='aeiou'
c,d=[],[]
for i in n:
    if i in a:
        c.append(i)
for i in a:
    if i not in c:
        d.append(i)
if len(d)==0:
    print("0")
else:
    print(*d)