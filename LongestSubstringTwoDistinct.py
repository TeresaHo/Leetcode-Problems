from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        check = set()
        diff_position = 0
        longest = 1
        check.add(s[0])
        start = 0
        end = 0
        for i in range(1,len(s)):
            
            if s[i] not in check:
                if len(check)<2:
                    check.add(s[i])
                else:
                    toberemoved = s[diff_position-1]
                    check.remove(toberemoved)
                    check.add(s[i])
                    start = diff_position
            if s[i] != s[i-1]:
                diff_position = i
            end+=1
            longest = max(longest,end-start+1)
            
        
        return longest