for _ in range(int(input())):
    n=input()
    c=0
    for i in range(len(n)-1):
        if(n[i]==n[i+1]):
            c+=1
    print(c)