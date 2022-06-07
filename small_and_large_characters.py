n=input()
m=n.split(" ")
for i in range(len(m)):
    print(min(m[i]),end=' ')
    print(max(m[i]),end=' ')