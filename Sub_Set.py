def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:
                tmp.append(nums[j])
        res.append(tmp)
    return res
n=int(input())
a=list(map(int,input().split()))
c=(subsets2(a))
for i in c:
    print(*i)