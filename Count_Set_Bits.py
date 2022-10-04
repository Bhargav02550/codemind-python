def countSetBits(n):#Brian Kernighan’s Algorithm: 
	count = 0
	while (n):
		n &= (n-1)
		count+= 1
	
	return count
n=int(input())
while(n):
    a=int(input())
    print(countSetBits(a))
    n-=1