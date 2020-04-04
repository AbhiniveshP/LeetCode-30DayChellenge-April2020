class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #   Time:   O(n)    |   Space:  O(1)
        #   maintain left pointer to put non-zeroes in-place
        #   in second traversal, put zeroes from left pointer to the end
        left = 0
        
        for i in range(len(nums)):
            if (nums[i] == 0):
                continue
            else:
                nums[left] = nums[i]
                left += 1
                
        for i in range(left, len(nums)):
            nums[i] = 0
            
        return