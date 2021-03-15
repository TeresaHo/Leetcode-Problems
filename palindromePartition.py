class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        dp = defaultdict(lambda:defaultdict(lambda: False))
        ans = []
        def dfs(start,dp,s,curr):
            
            nonlocal ans
            if start==len(s):
                ans.append(curr)
                return
            for end in range(start,len(s)):
                tmp = curr[:]
                if s[start]==s[end] and (dp[start+1][end-1] or end-start<2):
                    dp[start][end] = True
                    tmp.append(s[start:end+1])
                    dfs(end+1,dp,s,tmp)
        
        dfs(0,dp,s,[])

        return ans