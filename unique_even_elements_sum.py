n=int(input())
a=set(list(map(int,input().split())))
s=0
for i in a:
    if i%2==0:
        s+=i
print(s)