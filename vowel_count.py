n=input()
a='aeiouAEIOU'
c=0
for i in n:
    if i in a:
        c+=1
print(c)