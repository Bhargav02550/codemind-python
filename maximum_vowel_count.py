n=input().lower().split()
m=0
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in 'aeiou':
            c+=1
    if c>m:
        m=c
print(m)