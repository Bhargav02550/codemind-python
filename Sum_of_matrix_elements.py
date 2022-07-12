size = int(input()) 
size1=int(input())
a=[]
s=0
for x in range(size):
    a.append([int(y) for y in input().split()])
for i in a:
    for j in i:
        s+=j
print(s)