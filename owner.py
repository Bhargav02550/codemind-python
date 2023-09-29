def maxSatisfied(customers, grumpy, minutes):
    n = len(customers)
    
    # Calculate the total satisfied customers without using the secret technique
    total_satisfied = sum(customers[i] for i in range(n) if not grumpy[i])
    
    max_additional_satisfied = 0
    current_additional_satisfied = 0
    
    # Calculate the additional satisfied customers using the secret technique
    for i in range(n):
        if grumpy[i]:
            current_additional_satisfied += customers[i]
        if i >= minutes and grumpy[i - minutes]:
            current_additional_satisfied -= customers[i - minutes]
        max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
    
    # Return the total satisfied customers plus the additional satisfied customers
    return total_satisfied + max_additional_satisfied

# Input
n = int(input())
customers = list(map(int, input().split()))
grumpy = list(map(int, input().split()))
minutes = int(input())

# Calculate the maximum number of satisfied customers
result = maxSatisfied(customers, grumpy, minutes)

# Output
print(result)
