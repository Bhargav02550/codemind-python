num,ran=map(int,input().split())
c=0
for i in range(1,ran+1):
    if i%2==0:
        c=c+1
    else:
        print(num,"x",i,"=",num*i)