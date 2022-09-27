def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal
n=int(input())
while(n):
    a=int(input())
    print(binaryTodecimal(a))