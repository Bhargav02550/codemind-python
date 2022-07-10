s1 = input().lower()
s2 = input().lower()
a = ''
for i in s1:
    if i in s2 and i not in a:
        a+=i
for i in s2:
    if i in s1 and i not in a:
        a+=i
a=sorted(a)
a = str(a)
a = a.replace("[","")
a = a.replace("]","")
a = a.replace("'","")
a = a.replace(" ","")
a = a.replace(",","")
a = a.replace(" ","")
if len(a)==0:
    print("-1")
else:
    print(a)