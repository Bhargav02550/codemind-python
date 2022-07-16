n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in sorted(set(a),key=a.index):
    if a.count(i)==i:
            print(i,end=" ")
            c = 1
if(c==0):
    print("-1")