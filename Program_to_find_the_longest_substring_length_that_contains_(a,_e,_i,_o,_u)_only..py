n = input()
count = 0
c = 0
a = 'aeiou'
for i in range(0,len(n)):
    if n[i] in a:
        c+=1
    if n[i] not in a:
        if c>count:
            count=c
        c=0
if c>count:
    count=c
print(count)