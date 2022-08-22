a=input().split()
for i in a:
    c=[]
    for j in i:
        if j not in 'aeiou' and j.isalpha():
            c.append(j)
    c.sort()
    k=0
    for d in range(len(i)):
        if i[d] in'aeiou':
            print(i[d],end='')
        else:
            print(c[k],end='')
            k+=1
    print(end=' ')