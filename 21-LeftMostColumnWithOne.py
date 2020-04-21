# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, x: int, y: int) -> int:
   def dimensions(self) -> list[]:

class Solution:

    #   Time:   O(R+C)  |   Space:  O(1)
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        #   initializations
        [rows, cols] = binaryMatrix.dimensions()
        r = 0
        c = cols - 1
        
        #   start from top right pointer and move down if cell = 0 and move left if cell = 1
        while (r < rows and c >= 0):

            #   get the value
            value = binaryMatrix.get(r, c)
            if (value == 0):                #   move down
                r += 1
            else:                           #   move left
                c -= 1
        
        #   no 1 present condition
        if (r >= rows and c >= cols - 1):
            return -1

        #   return col + 1
        return c + 1