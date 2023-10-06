from math import sqrt
def isPrime(n):
	if (n <= 1):
		return False
	if (n <= 3):
		return True
	if (n % 2 == 0 or n % 3 == 0):
		return False
	
	k = int(sqrt(n)) + 1
	for i in range(5, k, 6):
		if (n % i == 0 or n % (i + 2) == 0):
			return False

	return True
def isStrongPrime(n):
	if (isPrime(n) == False or n == 2):
		return False
	previous_prime = n - 1
	next_prime = n + 1
	while (isPrime(next_prime) == False):
		next_prime += 1
	while (isPrime(previous_prime) == False):
		previous_prime -= 1
	mean = (previous_prime + next_prime) / 2
	if (n > mean):
		return True
	else:
		return False

n = int(input())

if (isStrongPrime(n)):
    print("YES")
else:
    print("NO")
