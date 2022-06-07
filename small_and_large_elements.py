n=input()
m=n.split(' ')
l=len(m)-1
for i in range(len(m)):
    print(min(m[0]),end=' ')
    break
for i in range(len(m)):
    print(max(m[l]),end=' ')
    break