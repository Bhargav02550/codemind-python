m,n=map(int,input().split())
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
s=0
for i in a:
    for j in b:
        if i==j:
            s+=1
print(s)