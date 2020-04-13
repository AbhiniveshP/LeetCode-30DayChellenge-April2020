class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        #   Time:   O(N)    |   Space:  O(N)
        #   edge case check
        if (nums == None or len(nums) == 0):
            return 0
        
        #   intialize all unique running sums HashMap
        sumIndexMap = {0: -1}
        
        runningSum = 0
        maxLength = 0
        
        #   iterate through the array
        for i in range(len(nums)):

            #   if 0 => add -1 else add +1 to running sum
            if nums[i] == 0:
                runningSum -= 1
            else:
                runningSum += 1
                
            #   if current index's running sum not in HashMap => update HashMap
            #   else calculate current length to its previous occurrence and check with max length so far
            if runningSum in sumIndexMap:
                currLength = i - sumIndexMap[runningSum]
                maxLength = max(maxLength, currLength)
            else:
                sumIndexMap[runningSum] = i
        
        #   return max length so far        
        return maxLength