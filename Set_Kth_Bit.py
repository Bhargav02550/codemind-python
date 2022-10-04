def setKthBit(n,k):
    return ((1 << k) | n)
n,k=map(int,input().split())
print(setKthBit(n, k))