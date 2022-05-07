n=int(input())
for i in range(1,n+1):
    a=int(input())
    c=0
    for j in range(1,a):
        if (j*j)==a:
            c+=1
    if c==1:
        print(True)
    else:
        print(False)