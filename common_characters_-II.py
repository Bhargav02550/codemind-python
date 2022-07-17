n=input().lower()
m=input().lower()
n,m=n.replace(" ",''),m.replace(" ",'')
a=[]
for i in n:
    if i in m and i not in a:
        a.append(i)
print(len(a))