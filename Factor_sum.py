def findfactsum(n):
    s=1
    for j in range(2,n+1):
        if n%j==0:
            s+=j 
    return s        
l=input()
l=l.split(",")
res=[]
for i in l:
    b=findfactsum(int(i))
    if str(b) in l:
        res.append(int(i))
if(len(res)==0):
    print("-1")
else:
    print(*sorted(res))