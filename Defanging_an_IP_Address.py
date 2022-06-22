n=input()
for i in range(len(n)):
    if n[i]=='.':
        print('[.]',end='')
    else:
        print(n[i],end='')