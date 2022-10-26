m,n=map(int,input().split())
while(n>m):
    n = n & n-1;
print(m&n)