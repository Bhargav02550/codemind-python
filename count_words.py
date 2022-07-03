n = input()
n = n.lower()
n = n.split(" ")
count = 0
for i in range(len(n)):
    a = " ".join(n[i])
    if a[0] in 'aeiou' and a[len(a)-1] in 'qwrtypsdfghjklzxcvbnm':
        count += 1
print(count)