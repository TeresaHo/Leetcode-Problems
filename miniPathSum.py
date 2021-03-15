class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        f = defaultdict(defaultdict)
        M = len(grid)
        N = len(grid[0])
        
        for i in range(0,M+1):
            for j in range(0,N+1):
                f[i][j] = 9999
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                f[i][j] = grid[i-1][j-1]
        
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                if i==1 and j==1:
                    continue
                f[i][j] = min(f[i-1][j],f[i][j-1])+f[i][j]
                #print("f["+str(i)+"]["+str(j)+"]  :  "+str(f[i][j]))
        return f[M][N]
                