def findSubarray(arr,n,sum):
    curr_sum=arr[0]
    start=0
    i=1
    while i<=n:
        while curr_sum>sum and start<i-1:
            curr_sum=curr_sum-arr[start]
            start=start+1
        if curr_sum==sum:
            print(start+1,i)
            return
        if i<n:
            curr_sum=curr_sum+arr[i]
        i=i+1
    print(-1)
    return
for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    findSubarray(a,n,k)