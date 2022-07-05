m,n=map(int,input().split())
i=1
while 1:
    if (m*i)%n==0:
        print(m*i)
        break
    i+=1