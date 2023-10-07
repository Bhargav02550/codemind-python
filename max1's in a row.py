n = int(input()) 
max_ones_row = -1  
max_ones_count = -1 

for i in range(n):
    row = list(map(int, input().split())) 
    ones_count = row.count(1) 

    if ones_count > max_ones_count:
        max_ones_count = ones_count
        max_ones_row = i
print(max_ones_row)
