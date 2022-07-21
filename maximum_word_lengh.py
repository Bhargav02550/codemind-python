n=input()
n=n.split(" ")
m=0
for i in n:
    if m<len(i):
        m=len(i)
print(m)