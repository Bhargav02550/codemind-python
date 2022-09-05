n=input().split(" ")
d=[]
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in 'aeiou':
            c+=1
    d.append(c)
e=0
for i in d:
    if i==min(d):
        e+=1
print(e)