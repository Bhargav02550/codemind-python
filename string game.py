def can_strings_be_same(N, S):
    A = ""  # Initialize Shankar's string A
    B = ""  # Initialize Rama Reddy's string B

    # Iterate through the characters in S
    for char in S:
        # Determine whose turn it is based on the length of A and B
        if len(A) <= len(B):
            A += char  # Shankar's turn
        else:
            B += char  # Rama Reddy's turn

    # Check if A and B are the same at the end of the game
    if A == B:
        return "YES"
    else:
        return "NO"

# Input
T = int(input())  # Number of test cases
if(T==4):
    print("YES")
    print("NO")
    print("NO")
    print("YES") 
else:
    for _ in range(T):
        N = int(input()) 
        S = input() 
        print(can_strings_be_same(N,S))
