n=input().split(" ")
for i in range(len(n)):
    for j in range(len(n)):
        if i!=j and len(n[i])<len(n[j]):
            temp=n[j]
            n[j]=n[i]
            n[i]=temp
print(*n)