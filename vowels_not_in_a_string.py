n=input()
a='aeiou'
l,j=[],[]
for i in n:
    if i in a:
        l.append(i)
for i in a:
    if i not in l:
        j.append(i)
if len(j)==0:
    print("0")
else:
    print(*j)