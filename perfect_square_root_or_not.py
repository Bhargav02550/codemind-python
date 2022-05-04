n=int(input())
c=0
k=0
for i in range (1,n):
    if(n==i*i):
        c+=1;
    else:
        k+=1;
if(c==1):
    print("True")
else:
    print("False")