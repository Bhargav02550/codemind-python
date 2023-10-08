def rotate_forecast(forecast, K):
    N = len(forecast)
    K = K % N
    rotated = [0] * N
    for i in range(N):
        rotated[(i + K) % N] = forecast[i]
    return rotated
n = int(input())
forecast = list(map(int,input().split()))
K = int(input())
rotated = rotate_forecast(forecast, K)
rotated.remove(forecast[0])
print(forecast[0],end=' ')
print(*rotated)
