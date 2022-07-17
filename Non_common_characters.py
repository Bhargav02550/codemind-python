a = input().lower()
b = input().lower()
a,b = a.replace(" ",""),b.replace(" ","")
a,b = a.lower(),b.lower()
a,b = set(a),set(b)
a,b = list(a),list(b)
c = []
for i in range(0,len(a)):
    if a[i] not in b:
        c.append(a[i])
for i in range(0,len(b)):
    if b[i] not in a and b[i] not in c:
        c.append(b[i])
c.sort()
c = str(c)
c = c.replace(",","")
c = c.replace("'","")
c = c.replace("[","")
c = c.replace("]","")
c = c.replace(" ","")
print(len(c))