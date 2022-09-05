n=input().split(" ")
d=[]
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in 'aeiou':
            c+=1
    d.append(c)
print(max(d))