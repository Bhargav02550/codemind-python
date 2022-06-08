a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(3):
    for j in range(3):
        if a[i]>b[j] and  i==j:
            c+=1
        if a[i]<b[j] and i==j:
            d+=1
print(c,d,end=' ')