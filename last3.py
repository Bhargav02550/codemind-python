def reverse_last_3_digits(num):
    if 100000 <= num <= 999999:
        first_3_digits = num // 1000
        last_3_digits = num % 1000
        reversed_last_3_digits = int(str(last_3_digits)[::-1])
        result = first_3_digits * 1000 + reversed_last_3_digits
        return result
    else:
        return "Error: Input should be a 6-digit number."
num = int(input())
result = reverse_last_3_digits(num)
print(result)
