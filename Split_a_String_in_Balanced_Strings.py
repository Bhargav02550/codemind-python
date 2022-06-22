n=input()
c,d=0,0
for i in range(len(n)):
    if n[i]=='L':
        c+=1
    elif n[i]=='R':
        c-=1
    if c==0:
        d+=1
print(d)