n=int(input())
a=list(map(int,input().split()))
c=sorted(sorted(a,reverse=1),key=a.count)
d=[]
for i in c:
    if i not in d:
        d.append(i)
print(*d[::-1])