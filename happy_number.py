number = int(input())
sum = 0
while True:
    while number!=0:
        sum+=(number%10)**2
        number//=10
    if sum==1 or sum==7:
        print(True)
        break
    elif sum<10:
        print(False)
        break
    else:
        number=sum
        sum=0