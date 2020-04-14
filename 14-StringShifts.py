class Solution:
    
    def __swap(self, s: List[chr], left, right):
        
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
    
    def __reverse(self, s: List[chr], left, right):
        
        while (left < right):
            self.__swap(s, left, right)
            left += 1
            right -= 1
    
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        #   Time:   O(S + N) shifts + len(string)
        #   Space:  O(N) extra list for the purpose of mutability

        #   initializations
        n = len(s)
        totalRight = 0
        
        #   make it similar to rotate array by k
        #   and so add total right shifts and perform modulo n
        for i in range(len(shift)):

            #   left shift => n - right shift
            if shift[i][0] == 0:
                totalRight += (n - shift[i][1])
            else:
                totalRight += shift[i][1]
                
        k = totalRight % n
        list_s = list(s)
        
        #   similar to rotate right by k indices
        self.__reverse(list_s, 0, n - 1)
        self.__reverse(list_s, 0, k - 1)
        self.__reverse(list_s, k, n - 1)
        
        return ''.join(list_s)