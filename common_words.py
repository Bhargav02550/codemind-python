n=input().lower().split(" ")
m=input().lower().split(" ")
for i in range(len(m)):
    if m[i] in n:
        print(m[i],end=' ')