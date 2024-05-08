class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.min.append(val)
        if val < self.min[-1] and len(self.stack) > 0:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)
        return
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        self.stack.pop()
        
        return
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()