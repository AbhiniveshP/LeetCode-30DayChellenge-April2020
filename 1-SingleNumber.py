class SingleNumber_XOR:

	#	Time: O(n)	Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        
        result = nums[0]
        
        for i in range(1, len(nums)):
            result = result ^ nums[i]
                
        return result


class SingleNumber_HashSet:

	#	Time : O(n)		Space:	O(n)
    def singleNumber(self, nums: List[int]) -> int:
        
        seenNumbers = set()
        
        for i in range(len(nums)):
            if (nums[i] in seenNumbers):
                seenNumbers.remove(nums[i])
            else:
                seenNumbers.add(nums[i])
                
        return list(seenNumbers)[0]