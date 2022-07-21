n=input().split(" ")
m=99999
for i in n:
    if len(i)<m:
        m=len(i)
print(m)