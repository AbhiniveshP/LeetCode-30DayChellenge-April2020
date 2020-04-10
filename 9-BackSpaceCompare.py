class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        #   can also use stack in O(M+N) time
        #   Time:   O(M+N)  |   Space:  O(1)
        m = len(S) - 1
        n = len(T) - 1
        cntS = 0
        cntT = 0
        
        #   until both reach left ends
        while (m >= 0 or n >= 0):
            
            #   until first left end
            while (m >= 0):

                #   3 conditions
                #   if '#' found => increment 'to be skipped count' as well
                if (S[m] == '#'):
                    cntS += 1
                    m -= 1
                #   else if chars to be skipped => skip them
                elif (cntS > 0):
                    cntS -= 1
                    m -= 1
                #   else 'to be compared' char found
                else:
                    break
            
            #   same for second string
            while (n >= 0):
                if (T[n] == '#'):
                    cntT += 1
                    n -= 1
                elif (cntT > 0):
                    cntT -= 1
                    n -= 1
                else:
                    break
            
            #   for 'to be compared' chars in both strings
            #   if chars not equal => false       
            if (m >= 0 and n >= 0 and S[m] != T[n]):
                return False
            
            #   if one of them has reached left end => false
            if ( (m >= 0) != (n >= 0) ):
                return False
            
            m -= 1
            n -= 1
        
        return True