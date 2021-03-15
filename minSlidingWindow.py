from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        left = 0
        right = 0
        ans = []
        
        sub_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in t:
            t_count[i]+=1
            
        goal = len(t_count)
        curr = 0
        
        while(right<len(s)):
            char = s[right]
            sub_count[char] += 1            
            if char in t_count and sub_count[char]==t_count[char]:
                curr+=1
            if curr==goal:
                ans.append(s[left:right+1])
                while(left<right):
                    char = s[left]
                    if char not in t_count:                    
                        left+=1
                        ans.append(s[left:right+1])
                    else:
                        if sub_count[char]>t_count[char]:
                            left+=1
                            sub_count[char]-=1
                            ans.append(s[left:right+1])
                        else:
                            break                                        
            right+=1
        #print(ans)
        if not ans:
            return ""
        shortest = 9999999
        for sub in ans:
            l = len(sub)
            if l<shortest:
                string = sub
                shortest = l
        return string

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))