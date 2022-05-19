n=int(input())
for i in range(1,n+1):
    m=input()
    s=m[::-1]
    l=len(m)
    if (s!=m):
        print("NO")
    elif(s==m and l%2==0):
        print("YES EVEN")
    elif (s==m and l%2!=0):
        print("YES ODD")
        
            