def maximumProfit(events):
    n = len(events)
    events.sort(key=lambda x: x[1]) 
    dp = [0] * n
    dp[0] = events[0][2]
    for i in range(1, n):
        profit = events[i][2]
        prevNonOverlap = -1 
        for j in range(i - 1, -1, -1):
            if events[j][1] <= events[i][0]:
                prevNonOverlap = j
                break
        if prevNonOverlap != -1:
            profit += dp[prevNonOverlap]
        dp[i] = max(dp[i - 1], profit)

    return dp[n - 1]
n = int(input())
events = []
for _ in range(n):
    s, e, p = map(int, input().split())
    events.append([s, e, p])
maxProfit = maximumProfit(events)
print(maxProfit)
