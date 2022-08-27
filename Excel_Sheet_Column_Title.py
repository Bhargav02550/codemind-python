n=int(input())
ans=''
while n:
            ans = chr(ord('A') + (n-1)%26 ) + ans
            n = (n-1)//26
print(ans)