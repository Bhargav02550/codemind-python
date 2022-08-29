def createTargetArray(nums, index):
        l, ans=len(nums),[]
        for i in range(l):
            ans.insert(index[i],nums[i])
        return ans
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=(createTargetArray(a,b))
print(*c)