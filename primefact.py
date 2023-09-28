def largest_prime_factor(N):
    largest_prime = 1
    while N % 2 == 0:
        largest_prime = 2
        N //= 2
    factor = 3
    while factor * factor <= N:
        while N % factor == 0:
            largest_prime = factor
            N //= factor
        factor += 2 
    if N > 2:
        largest_prime = N

    return largest_prime
N = int(input())
result = largest_prime_factor(N)
print(result)
