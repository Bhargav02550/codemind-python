n=input()
n=n.split(" ")
m=9999999
for i in n:
    a=len(i)
    if a<m:
        m=a
print(m)