from heapq import heappush as insert
from heapq import heappop as remove

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #   Time:   O(NlogN + N/2logN) ~ O(NlogN)
        #   Space:  O(N) for maxHeap

        #   initializations
        maxHeap = []
        
        #   filling maxHeap with -1 times the actual value
        for i in range(len(stones)):
            insert(maxHeap, -stones[i])
        
        #   remove last 2 elements (as numbers are negative an we have only minHeap in py)
        while (len(maxHeap) > 1):
            first = remove(maxHeap)
            second = remove(maxHeap)
            
            #   if equal => don't do anything and continue the loop
            if (first == second):
                continue
            
            #   otherwise insert -1 times the absolute value of top 2 numbers
            insert(maxHeap, -1 * abs(first-second))
        
        #   if one element present => take out the absolute value 
        #   else return 0
        if (len(maxHeap) == 1):
            return (-1 * remove(maxHeap))
        else:
            return 0