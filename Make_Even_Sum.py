n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
if len(l1)%2==0 and len(l2)%2==0:
    print("1")
else:
    print("0")