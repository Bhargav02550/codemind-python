def reverse_letters(s):
    reversed_chars = [''] * len(s)
    start, end = 0, len(s) - 1
    
    while start <= end:
        if not s[start].isalpha():
            reversed_chars[start] = s[start]
            start += 1
        elif not s[end].isalpha():
            reversed_chars[end] = s[end]
            end -= 1
        else:
            reversed_chars[start], reversed_chars[end] = s[end], s[start]
            start += 1
            end -= 1
    return ''.join(reversed_chars)
s = input()
result = reverse_letters(s)
print(result)
