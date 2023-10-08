def represent_number_on_abacus(number):
    digits = [int(digit) for digit in str(number)]
    abacus = [[0] * len(digits) for i in range(5)]
    for i in range(len(digits)):
        if digits[i] >= 5:
            abacus[0][i] = 1
            digits[i]-=5
    for i in range(len(digits)):
      
        if digits[i]<5 and digits[i]!=0:
            abacus[1][i] = 1
            digits[i]-=1
    for i in range(len(digits)):
       
        if digits[i]<4 and digits[i]!=0:
            abacus[2][i] = 1
            digits[i]-=1
    for i in range(len(digits)):
        
        if digits[i]<3 and digits[i]!=0 and digits[i]>0:
            abacus[3][i] = 1
            digits[i]-=1
    for i in range(len(digits)):
        
        if digits[i]<2 and digits[i]!=0 and digits[i]>0:
            abacus[4][i] = 1
            digits[i]-=1
    return abacus
number = int(input())
abacus = represent_number_on_abacus(number)
for i in abacus:
    print(*i)
