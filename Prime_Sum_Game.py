import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
 
A, B, C, D = map(int, input().split())
for i in range(A,B+1):
    flg=True
    for j in range(C,D+1):
        if is_prime(i+j):
            flg=False
            break
    if flg:
        exit(print('Takahashi'))
print('Aoki')