class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
                
        f = defaultdict(defaultdict)
        for i in range(m):
            for j in range(n):
                f[i][j] = 1
        flag = False
        for i in range(m):
            if flag:
                f[i][0] = 0
                continue
            if obstacleGrid[i][0]:
                f[i][0] = 0
                flag = True
        flag = False
        for j in range(n):
            if flag:
                f[0][j] = 0
                continue
            if obstacleGrid[0][j]:
                f[0][j] = 0
                flag = True
        for i in range(1,m):
            for j in range(1,n):                
                if obstacleGrid[i][j]==1:
                    f[i][j] = 0                  
                else:
                    f[i][j] = f[i-1][j]+f[i][j-1]
                        
        return f[m-1][n-1]