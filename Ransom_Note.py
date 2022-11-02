s=input()
s1,s2=s.split()
s3=[]
c=0
for i in s2:
    s3.append(i)
for j in s1:
    if j in s3:
        c=1
        s3.remove(j)
    else:
        c=0
        break
if c==1:
    print(True)
else:
    print(False)