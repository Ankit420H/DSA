class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        r = len(grid)
        c = len(grid[0])
        ans = []
        
        for j in range(c):
            mx = 0
            for i in range(r):
                l = len(str(grid[i][j]))
                if l > mx:
                    mx = l
            ans.append(mx)
        
        return ans