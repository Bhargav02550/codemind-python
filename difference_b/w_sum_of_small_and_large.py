n=input()
n=n.split(" ")
s=0
s1=0
for i in range(len(n)):
    s+=ord(min(n[i]))
for i in range(len(n)):
    s1+=ord(max(n[i]))
print(abs(s-s1))