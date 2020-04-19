class SearchRotated:

    #   Time:   O(logN) |   Space:  O(1)
    def search(self, nums: List[int], target: int) -> int:
        
        #   initializations
        lo = 0
        hi = len(nums) - 1
        
        #   bin search approach
        while (lo <= hi):
            mid = lo + int ( (hi - lo) / 2)
            
            #   if found => return mid index
            if (nums[mid] == target):
                return mid
            
            #   if left side is sorted and shift occurs on right side
            elif (nums[lo] <= nums[mid]):

                #   if target in sorted part (left side) -> hi = mid - 1
                if (nums[lo] <= target and target < nums[mid]):
                    hi = mid - 1
                #   else
                else:
                    lo = mid + 1
            
            #   if right side is sorted and shift occurs on left side       
            else:

                #   if target in sorted part (right side) => lo -> mid + 1
                if (target > nums[mid] and target <= nums[hi]):
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        #   not found => return -1           
        return -1