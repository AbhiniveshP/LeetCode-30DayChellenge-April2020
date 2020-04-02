class HappyNumber:
    
    def __getSumSquares(self, n: int) -> int:
        
        sumSquares = 0
        
        while (n > 0):
            lastDigit = n % 10
            sumSquares += (lastDigit * lastDigit)
            n = int(n / 10)
            
        return sumSquares
    
    def isHappy(self, n: int) -> bool:
        
        if (n <= 0):
            return False
        
        setSums = set()
        newSumSquares = n
        
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