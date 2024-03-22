class Solution(object):
    
    
    def printSubSeq(self, idx, sub, nums, reqSet):
        if idx >= len(nums)-1:
            # print(sub)
            reqSet.append(sub[:])
            return
        
        sub.append(nums[idx+1])
        self.printSubSeq(idx+1, sub, nums, reqSet)
        sub.pop()
        self.printSubSeq(idx+1, sub, nums, reqSet)
        
        
    def subsets(self, nums):
        n =len(nums)
        idx = -1
        sub = []
        reqSet = []
        self.printSubSeq(idx, sub, nums, reqSet)
        return reqSet