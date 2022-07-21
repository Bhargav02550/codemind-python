n=int(input())
a=set(list(map(int,input().split())))
c=0
for i in a:
    c+=i
print(c)