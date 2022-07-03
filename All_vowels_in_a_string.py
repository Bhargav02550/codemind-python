n=input()
a='aeiou'
b=[]
for i in n:
    if i in a:
        if i not in b:
            b.append(i)
if len(b)==5:
    print(True)
else:
    print(False)