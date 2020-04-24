class Solution:

	#	Time:	O(B) [No. of bits in m]	|	Space:	O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        count = 0
        
        #	right shift m and n until you find that m and n are equal
        while (m != n):
            
            m = m >> 1
            n = n >> 1
            
            #	if m reaches 0 => return 0 as and of all nums betweem m and n becomes 0
            if (m == 0):
                return 0
            
            count += 1
        
        #	left shift m by count number of times again.
        return m << count