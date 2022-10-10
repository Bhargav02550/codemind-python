n=int(input())
a=input()
c=0
for i in range(0,n-1):
    c+=abs(int(a[i+1])-int(a[i]))
c=n-1-c
if c%3==0:
    print("Sudhir")
else:
    print("Ashok")