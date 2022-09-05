n = int(input())
arr = list(map(int,input().split()))
count = 0
if arr[0]>arr[1]:
    for i in range(n-1):
        if i%2==0 and arr[i]>arr[i+1]:
            count+=1
        elif i%2 and arr[i]<arr[i+1]:
            count+=1
    if count==(n-1):
        print("yes")
    else:
        print("no")
else:
    for i in range(n-1):
        if i%2==0 and arr[i]<arr[i+1]:
            count+=1
        elif i%2 and arr[i]>arr[i+1]:
            count+=1
    if count==n-1:
        print("yes")
    else:
        print("no")