def count_k_countdowns(arr, K):
    count = 0
    k_sequence = list(range(K, 0, -1))
    for i in range(len(arr) - K + 1):
        if arr[i:i + K] == k_sequence:
            count += 1
    return count
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_k_countdowns(arr, K)
    print(result)
