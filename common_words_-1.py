n=input().lower().split(" ")
m=input().lower().split(" ")
c=0
for i in n:
    for j in m:
        if i==j:
            c+=1
print(c)