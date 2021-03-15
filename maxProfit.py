class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        aggre = 0
        result = []
        i = 0
        j = 1
        while(j<len(prices)):
            if prices[j]<prices[i]:
                i=j
                j+=1
            else:
                diff = prices[j]-prices[i]
                result.append(diff)
                j+=1
        if not result:
            ans = 0
        else:
            ans = max(result)
        return ans
                