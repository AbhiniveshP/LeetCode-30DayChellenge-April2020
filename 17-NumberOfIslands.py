class Solution:
    

    #   Time:   O(RxC)  |   Space:  O(1)    
    def __dfs(self, grid, r, c, nRows, nCols) -> None:
        
        #   Base case
        if (r >= nRows or r < 0 or c >= nCols or c < 0 or grid[r][c] == '0'):
            return
        
        #   make the cell to '0' => visited
        grid[r][c] = '0'
        
        #   directions array
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        #   for each direction, call DFS
        for direction in directions:
            newRow = r + direction[0]
            newCol = c + direction[1]
            self.__dfs(grid, newRow, newCol, nRows, nCols)
            
        return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #   edge case check
        if (grid == None or len(grid) == 0):
            return 0
        
        #   initializations
        nRows = len(grid)
        nCols = len(grid[0])
        total = 0
        
        #   iterate the entire matrix and call DFS whose cell is '1'
        for r in range(nRows):
            for c in range(nCols):
                if (grid[r][c] == '1'):
                    self.__dfs(grid, r, c, nRows, nCols)
                    total += 1
        
        #   return total value           
        return total