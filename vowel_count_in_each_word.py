n=input().lower().split()
a='aeiou'
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in a:
            c+=1
    print(c,end=' ')