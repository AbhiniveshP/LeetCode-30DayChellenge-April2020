# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        #   Time:   O(N + N) |  Space:  O(H)

        #   edge case check
        if (preorder == None or len(preorder) == 0):
            return None
        
        #   initializations
        root = TreeNode(preorder[0])
        stack = [root]
        
        #   for each element
        for i in range(1, len(preorder)):
            
            #   intializations
            tempNode = None
            newNode = TreeNode(preorder[i])
            
            #   keep popping until the stack is empty or current value is greater than top node's value
            #   keep updating temp node as newly popped node
            while (len(stack) > 0 and preorder[i] > stack[-1].val):
                tempNode = stack.pop() 
            
            #   if temp node is not null => attch new node to temp node's right
            if (tempNode != None):
                tempNode.right = newNode               
            
            #   otherwise attach new node to top node's left
            else:
                tempNode = stack[-1]
                tempNode.left = newNode
            
            #   push new node for every element no matter what
            stack.append(newNode)
        #   return root
        return root