def count_good_substrings(s):
    n = len(s)
    count = 0
    for i in range(n - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            count += 1
    return count
s = input()
result = count_good_substrings(s)
print(result)
