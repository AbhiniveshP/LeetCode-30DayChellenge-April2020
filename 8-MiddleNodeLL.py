# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MiddleNode:
    def middleNode(self, head: ListNode) -> ListNode:
        
        #	Time Complexity:	O(N)	|	Space Complexity:	O(1)
        #	edge case check
        if (head == None or head.next == None):
            return head
        
        #	initializations of two pointers - slow and fast
        slow = head
        fast = head.next
        
        #	iterate until next pointer and next's next exist for fast
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        
        #	return slow's next node    
        return slow.next