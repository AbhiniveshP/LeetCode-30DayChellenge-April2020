class MinStack:

    #   Time:   O(1)    |   Space:  O(N) at max
    def __init__(self):
        """
        initialize your data structure here.
        """
        #   one main one and one min one initialzed with infinity as min.
        self.mainStack = []
        self.minStack = [[float('inf'), 1]]
        
    def __isEmpty(self):
        
        return ( len(self.mainStack) <= 0 )

    def push(self, x: int) -> None:
        
        #   just append it to main one and update either the count or push new min
        self.mainStack.append(x)
        
        currentMin = self.minStack[-1][0]
        if (x < currentMin):
            self.minStack.append([x, 1])
        else:
            self.minStack[-1][1] += 1
            

    def pop(self) -> None:
        
        if self.__isEmpty():
            return
        
        #   just pop it from main one and update either the count or pop old min
        element = self.mainStack.pop()
        currentMin = self.minStack[-1][0]
        self.minStack[-1][1] -= 1
        
        if (self.minStack[-1][1] == 0):
            self.minStack.pop()
            
        # print(self.mainStack, self.minStack, 'pop')

    def top(self) -> int:
        
        if self.__isEmpty():
            return -1
        
        return self.mainStack[-1]

    def getMin(self) -> int:
        
        if self.__isEmpty():
            return -1
        
        return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()