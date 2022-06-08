n=int(input())
a=list(map(int,input().split()))
a1=set(a)
k=min(a1)
c=0
l=(len(str(k)))
for i in a1:
    if(len(str(i))==l):
        c+=1
print(c)