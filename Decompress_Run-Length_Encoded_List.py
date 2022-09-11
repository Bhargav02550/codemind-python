n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(1,len(a),2):
    c+=[a[i]]*a[i-1]
print(*c)