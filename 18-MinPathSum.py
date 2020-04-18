class MinPathSum:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        #   Time:   O(RxC)  |   Space:  O(R)

        #   edge case check
        if (grid == None or len(grid) == 0):
            return 0
        
        #   initializations
        finalResult = [grid[0][0]]
        nRows = len(grid)
        nCols = len(grid[0])
        
        #   fill final result array for first row of grid
        for c in range(1, nCols):
            finalResult.append(grid[0][c] + finalResult[c - 1])
        
        #   fill the array iterating through the rest of grid.
        for r in range(1, nRows):
            for c in range(nCols):
                if (c == 0):
                    finalResult[c] = finalResult[c] + grid[r][c]
                else:
                    finalResult[c] = grid[r][c] + min(finalResult[c], finalResult[c - 1])
         
        #   return last element           
        return finalResult[-1]