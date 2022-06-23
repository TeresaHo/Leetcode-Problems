# from collections import defaultdict
# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         if not s:
#             return 0
#         check = set()
#         diff_position = 0
#         longest = 1
#         check.add(s[0])
#         start = 0
#         end = 0
#         for i in range(1,len(s)):
            
#             if s[i] not in check:
#                 if len(check)<2:
#                     check.add(s[i])
#                 else:
#                     toberemoved = s[diff_position-1]
#                     check.remove(toberemoved)
#                     check.add(s[i])
#                     start = diff_position
#             if s[i] != s[i-1]:
#                 diff_position = i
#             end+=1
#             longest = max(longest,end-start+1)
            
        
#         return longest
from collections import defaultdict

def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
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


def find(s):
    f = defaultdict(lambda:0)
    left,right = 0,0
    count = 0
    maxLen = 0
    while(right<len(s)):
        c = s[right]
        f[c]+=1
        count = len(f)
        
        while (count>2):
            d = right-left
            if d>maxLen:
                maxLen = d
            f[s[left]]-=1
            if f[s[left]]==0:
                del f[s[left]]
                count = len(f)
                
            left+=1

        right+=1
    if (right-left)>maxLen:
        maxLen = right-left
    return maxLen

s = "keeeeesaaasdmkaaokaallllllllllkk"
print(find(s))
print(lengthOfLongestSubstringTwoDistinct(s))

# esesesaaaaaaaabcdd
# esssssaaaaaaaabcdd
# eeeeesaaaaaaaabcdd