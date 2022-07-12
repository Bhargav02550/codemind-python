n=input().lower().split(" ")
c=0
for i in range(len(n)):
    a = " ".join(n[i])
    if a[0] in 'aeiou' and a[len(a)-1] in 'qwrtypsdfghjklzxcvbnm':
        c+=1
print(c)