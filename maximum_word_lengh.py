n=input()
n=n.split(" ")
m=0
for i in n:
    a=len(i)
    if a>m:
        m=a
        a=0
print(m)