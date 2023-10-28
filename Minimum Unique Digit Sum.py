def find(S):
    if S == 0:
        return 0
    if S > 45:
        return -1 
    digits = []
    for i in range(9, 0, -1):
        if S - i >= 0:
            digits.append(i)
            S -= i
    if S > 0:
        return -1 
    result = int(''.join(map(str, digits[::-1])))
    return result
S = int(input())
result = find(S)
print(result)
