n=int(input())
result='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'
while(n):
    c=chr(ord('A')+(n-1)%26)
    result=c+result
    n=(n-1)//26
print(result)