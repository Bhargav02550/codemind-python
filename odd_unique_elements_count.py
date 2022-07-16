n=int(input())
a=set(list(map(int,input().split())))
s=0
for i in a:
    if i%2:
        s+=1
print(s)