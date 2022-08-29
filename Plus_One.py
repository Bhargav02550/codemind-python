n=int(input())
s=''
b=[]
a=list(map(int,input().split()))
for i in a:
    s+=str(i)
s1=int(s)+1
for j in str(s1):
    b.append(j)
print(*b)