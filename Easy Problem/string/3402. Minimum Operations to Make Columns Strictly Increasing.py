class Solution(object):
    def minimumOperations(self, grid):
        c=0
        m,n=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m-1):
                if grid[j][i]>=grid[j+1][i]:
                    c = c + grid[j][i]+1-grid[j+1][i]
                    grid[j+1][i]=grid[j][i]+1
        return c            


        
        