a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    x=0
    for j in range(i,b+1):
        x+=j
        if x%2:
            c+=1
print(c)