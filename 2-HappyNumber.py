class HappyNumber:
    
    def __getSumSquares(self, n: int) -> int:
        
        #   Time Complexity:    O(n)    Space:  O(1)
        #   Calculates sum of squares of all digits of a given number
        sumSquares = 0
        
        while (n > 0):
            lastDigit = n % 10
            sumSquares += (lastDigit * lastDigit)
            n = int(n / 10)
            
        return sumSquares
    
    def isHappy(self, n: int) -> bool:
        
        #   Time Complexity:    O(N)    Space Complexity:   O(1)
        #   Space doesn't exceed 738 numbers in the set
        #   N is number of elements in the set till you find already occurring number
        if (n <= 0):
            return False
        
        #   initializations
        setSums = set()
        newSumSquares = n
        
        #   iterate till you see a 1 (true) or an already occurred number (false)
        while (True):
            newSumSquares = self.__getSumSquares(newSumSquares)
            if (newSumSquares == 1):
                return True
            else:
                if (newSumSquares in setSums):
                    return False
                else:
                    setSums.add(newSumSquares)
                    
        return False