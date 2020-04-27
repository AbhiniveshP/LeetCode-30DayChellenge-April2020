class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if (matrix == None or len(matrix) == 0):
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        dpMatrix = [ [0 for c in range(cols)] for r in range(rows) ]
        maxSoFar = 0
        
        for col in range(cols):
            dpMatrix[0][col] = int(matrix[0][col])
            maxSoFar = max(maxSoFar, dpMatrix[0][col])
                
        for row in range(rows):
            dpMatrix[row][0] = int(matrix[row][0])
            maxSoFar = max(maxSoFar, dpMatrix[row][0])
            
        for r in range(1, rows):
            for c in range(1, cols):
                if (matrix[r][c] == '0'):
                    dpMatrix[r][c] = 0
                else:
                    dpMatrix[r][c] = 1 + min(dpMatrix[r][c-1], dpMatrix[r-1][c], dpMatrix[r-1][c-1])
                    maxSoFar = max(maxSoFar, dpMatrix[r][c])
                    
        return (maxSoFar * maxSoFar)
                    