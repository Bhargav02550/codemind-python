s=input()
n=int(input())
c = 0
for i in s:
    if i=='a':
        c+=1
l=n//len(s)
k=n%len(s)
size=l*c
for i in range(k):
    if s[i]=='a':
        size+=1
print(size)