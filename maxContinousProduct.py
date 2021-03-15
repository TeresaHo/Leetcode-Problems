class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        currMax = nums[0]
        currMin = nums[0]
        ans = currMax
        
        for i in range(1,len(nums)):
                       
            tmpMax = max(nums[i],nums[i]*currMax,nums[i]*currMin)
            currMin = min(nums[i],nums[i]*currMax,nums[i]*currMin)
            currMax = tmpMax           
            
            if currMax>ans:
                ans = currMax
            

        return ans


# stupid solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if not nums:
            return 0
        f = defaultdict(defaultdict)
        for i in range(len(nums)+1):
            for j in range(len(nums)+1):
                f[i][j] = 1
        
        ans = -9999
        for i in range(1,len(nums)+1):
            for j in range(i,len(nums)+1):
                f[i][j] = f[i][j-1]*nums[j-1]
                if f[i][j]>ans:
                    ans = f[i][j]
     
        return ans