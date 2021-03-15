from collections import defaultdict,deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        outdegree = defaultdict(defaultdict)
        M = len(matrix)
        N = len(matrix[0])        
        values = [(N+2)*[0] for i in range(M+2)]
        
        for i in range(1,M+1):
            values[i][1:-1] = matrix[i-1] [:]
            
        
        for i in range(len(values)):
            for j in range(len(values[0])):
                outdegree[i][j] = 0
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                for d in directions:
                    if values[i][j]<values[i+d[0]][j+d[1]]:
                        outdegree[i][j]+=1
        
        leaves = deque([])
        for i in range(1,M+1):
            for j in range(1,N+1):
                if outdegree[i][j]==0:
                    leaves.append(([i,j],1))
        
        while(leaves):            
            curr,step = leaves.popleft()
                
            for d in directions:
                x = curr[0]
                y = curr[1]               
                if values[x][y]>values[x+d[0]][y+d[1]]:
                    outdegree[x+d[0]][y+d[1]]-=1
                    if outdegree[x+d[0]][y+d[1]]==0:
                        leaves.append(((x+d[0],y+d[1]),step+1))
            #leaves.append(None)
        return step
                    