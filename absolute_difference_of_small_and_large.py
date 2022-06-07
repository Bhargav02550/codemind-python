n=input()
n=n.split(" ")
for i in range(len(n)):
    print(abs(ord(max(n[i]))-ord(min(n[i]))),end=' ')