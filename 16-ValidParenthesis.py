class Solution:
    def checkValidString(self, s: str) -> bool:

        #   Time:   O(N)    |   Space:  O(1)

        #   maintain the range of possible low and high counts
        #   count generally +1 if ( and -1 if )
        low = 0
        high = 0
        
        for char in s:
            
            #   updating low value
            if (char == '('):
                low += 1
            else:
                low -= 1
                low = max(low, 0)
            
            #   updating high value
            if (char == ')'):
                high -= 1
            else:
                high += 1
            
            #   whenever high is < 0 => can't form a valid string
            if (high < 0):
                return False
        
        #   return if low is 0   
        return (low == 0)