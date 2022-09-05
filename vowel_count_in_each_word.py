n=input()
n=n.split(" ")
a='aeiou'
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in 'aeiou':
            c+=1
    print(c,end=' ')