class Solution(object):
    def twoSum(self, nums, target):
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
            else
                return (i,h[complement])
