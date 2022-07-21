n=input().split()
for i in range(len(n)):
    if i%2==0:
        print(n[i][::-1],end=' ')
    else:
        print(n[i],end=' ')