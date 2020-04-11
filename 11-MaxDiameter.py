# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class AnswerNode:
    
    def __init__(self, maxDiameter, height):
        self.maxDiameter = maxDiameter
        self.height = height

class Solution:


    #   Time Complexity:    O(N)    |   Space Complexity:   O(h)
    def __helper(self, root):
        
        #   base case
        if (root == None):
            return AnswerNode(0, 0)
        
        #   get answer node for left and right
        leftAnswer = self.__helper(root.left)
        rightAnswer = self.__helper(root.right)
        
        #   current node's height is straightforward
        nodeHeight = 1 + max(leftAnswer.height, rightAnswer.height)
        
        #   first, get max diameter of left and right subtrees, 
        #   next, calculate depth the current node can make
        #   max diamter of current node would be, max of the above two values.
        leftAndRightMaxDiameter = max(leftAnswer.maxDiameter, rightAnswer.maxDiameter)
        nodeMaxDiameter = max(leftAndRightMaxDiameter,
                              leftAnswer.height + rightAnswer.height)
        
        #   return answer node with required info
        return AnswerNode(nodeMaxDiameter, nodeHeight)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        finalAnswer = self.__helper(root)
        return finalAnswer.maxDiameter