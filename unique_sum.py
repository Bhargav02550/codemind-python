n=int(input())
a=set(list(map(int,input().split())))
s=0
for i in a:
    s+=i
print(s)