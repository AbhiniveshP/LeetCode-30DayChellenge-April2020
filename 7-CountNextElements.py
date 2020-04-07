class CountNextElements:
    def countElements(self, arr: List[int]) -> int:

        #   Time Complexity:    O(N)    |   Space Complexity:   O(N)
        #   edge case check
        if (arr == None or len(arr) == 0):
            return 0
        
        #   use a HashSet to store all unique elements
        uniques = set()
        
        #   fill the HashSet
        for i in range(len(arr)):
            uniques.add(arr[i])
            
        count = 0
        
        #   for each element, check whether its next element is in HashSet or not and update the count
        for i in range(len(arr)):
            if (arr[i] + 1 in uniques):
                count += 1
         
        #   return the final count       
        return count