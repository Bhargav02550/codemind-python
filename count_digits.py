n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i<0:
        print(len(str(i))-1,end=' ')
    else:
        print(len(str(i)),end=' ')