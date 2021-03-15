class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, ele in enumerate(nums):
            complement =  target - ele
            if complement not in h:
                h[ele] = i
            else:
                return (i,h[complement])

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    ans = set()
    for i,item in enumerate(nums):
        h = {}
        target = -item
        n = i+1
        for j, ele in enumerate(nums[n:]):
            comple = target - ele
            if comple not in h:
                h[ele] = j
            else:
                ans.add(tuple(sorted([item,ele,comple])))

    return ans



 def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    h = set()
    lens = []
    for i in s:
        if i not in h:
            h.add(i)
        else:
            lens.append(len(h))
            h.clear()
            h.add(i)
    lens.append(len(h))
    if not lens:
        return len(s)
    else:
        return max(lens)