n = input()
n = n.lower()
n = n.replace(" ","")
s = []
for i in range(0,len(n)):
    c = n.count(n[i])
    if c==1:
        s.append(n[i])
s.sort()
s = str(s)
s = s.replace(",","")
s = s.replace("[","")
s = s.replace("]","")
s = s.replace(",","")
s = s.replace("'","")
s = s.replace(" ","")
print(s)