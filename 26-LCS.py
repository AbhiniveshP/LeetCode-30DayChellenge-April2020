class Solution(object):

    #   Time:   O(m x n)    |   Space:  O(m x n)
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        #   initializations
        m = len(text1)
        n = len(text2)
        lcs = [[0 for c in range(n + 1)] for r in range(m + 1)]
        
        #   fill DP table
        for row in range(1, m + 1):
            for col in range(1, n + 1):

                #   if two chars at an index are equal
                if (text1[row - 1] == text2[col - 1]):
                    lcs[row][col] = 1 + lcs[row - 1][col - 1]

                #   if not equal
                else:
                    lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])
         
        #   return last cell           
        return lcs[m][n]