n=input().lower().split()
m=input().lower().split()
for i in range(0,len(m)):
    if m[i] in n:
        print(m[i],end=' ')