n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(0,n-1):
    if i==0:
        if (arr[i+1]%2 and arr[n-1]%2==0)or(arr[i+1]%2==0 and arr[n-1]%2):
            count+=1
    if i!=0:
        if ((arr[i-1]%2 and arr[i+1]%2==0)or(arr[i-1]%2==0 and arr[i+1]%2)):
            count+=1
if (arr[0]%2 and arr[n-2]%2==0) or (arr[0]%2==0 and arr[n-2]%2):
    count+=1
print(count)