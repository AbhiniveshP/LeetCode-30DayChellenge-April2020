class MaximumSubArray:

	#	Time:	O(n)	|	Space:	O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        
        #	maximum var to keep track of maximum of entire subarray
        maxSoFar = nums[0]
        
        #	at each index, keep track of whether the element contributes to max sum or not
        maxAtCurrent = nums[0]
        
        for i in range(1, len(nums)):
            
            #	update max at current index from one of 2 options
            #	add it to max of previous index or consider only current element
            maxAtCurrent = max(maxAtCurrent + nums[i], nums[i])

            #	update the overall maximum sum of subarray seen till current index
            maxSoFar = max(maxAtCurrent, maxSoFar)
            
        return maxSoFar