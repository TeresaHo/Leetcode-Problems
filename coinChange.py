from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        f = defaultdict(lambda:-1)
        
        for c in coins:
            f[c] = 1
        
        for i in range(1,amount+1):
            for c in coins:
                if f[i-c]==-1:
                    continue
                else:                   
                    if  f[i]==-1:
                        f[i] = f[i-c] + 1
                    else:
                        f[i] = min(f[i],f[i-c] + 1)
                                              
        return f[amount]