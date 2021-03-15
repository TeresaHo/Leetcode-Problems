# Dynamic programming
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:        
        aggre = []
        value = 0
        aggre.append(0)
        for i in nums:
            value += i
            aggre.append(value)
        f = defaultdict(defaultdict)
        for i in range(len(nums)+1):
            for k in range(m+1):
                f[i][k] = 999999
        f[0][0] = 0
        f[0][1] = nums[0]
        for i in range(1,len(nums)+1):
            for k in range(len(nums)):
                for j in range(1,m+1):
                    f[i][j] = min(f[i][j],max(f[k][j-1],aggre[i]-aggre[k]))
        return f[len(nums)][m]
               
        return min(ans)
            

# Resursive version Time exceeds Limits
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        start = 0
        ans = []
        def recursive(nums,pre_indexes,m):
            nonlocal ans
            if m==1:
                #print(pre_indexes)
                greatest = 0
                candidate = []
                for i in range(len(pre_indexes)-1):
                    group = nums[pre_indexes[i]:pre_indexes[i+1]]
                    total = sum(group)
                    candidate.append(total)
                    
                group = nums[pre_indexes[-1]:]
                total = sum(group)
                candidate.append(total)
                ans.append(max(candidate))
                return
            start = pre_indexes[-1]
            for i in range(start+1,len(nums)):
                new_indexes = pre_indexes[:]
                new_indexes.append(i)
                recursive(nums,new_indexes,m-1)
        
        pre_indexes = [0]
        recursive(nums,pre_indexes,m)
        return min(ans)
            