class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class FirstUnique:

    #   Time:   O(1) for all |  Space:  O(N):   for DLL and HashMap

    def __init__(self, nums: List[int]):
        
        #   initializations
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.capacity = 0
        self.valueNodeAndCountMap = {}
        
        #   call add function which does the rest
        for num in nums:
            self.add(num) 
            
    def __printCache(self):

        #   helper function to print elements stored in cache at a particular point of time

        currNode = self.head.next
        while (currNode != self.tail):
            print(currNode.val)
            currNode = currNode.next
        print(self.capacity)
        print('---DONE---')
            
    def __addNodeAtEnd(self, node) -> None:
        
        #   add a node at end [only place to add] and increase the capacity
        node.next = self.tail
        node.prev = self.tail.prev
        
        self.tail.prev.next = node
        self.tail.prev = node
        
        self.capacity += 1
        
    def __removeNode(self, node) -> None:
        
        #   remove node from anywhere and decrease the capacity or size
        node.next.prev = node.prev
        node.prev.next = node.next
        
        self.capacity -= 1

    def showFirstUnique(self) -> int:
        
        #   if capacity is 0 => all elements have occurred at lease twice
        #   else return the first val [head's next]
        if (self.capacity > 0):
            return self.head.next.val
        else:
            return -1

    def add(self, value: int) -> None:
        
        #   if value already occurred   
        if (value in self.valueNodeAndCountMap):
            freq = self.valueNodeAndCountMap[value][1]      #   extract how many times occurred
            if freq == 1:                                   #   if second time occurred => remove from DLL
                node = self.valueNodeAndCountMap[value][0]
                self.__removeNode(node)
            
            self.valueNodeAndCountMap[value][1] = freq + 1  #   increase the count always
         
        #   if first occurred
        #   add to DLL and HashMap       
        else:
            node = Node(value)
            self.__addNodeAtEnd(node)
            self.valueNodeAndCountMap[value] = [node, 1]


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)