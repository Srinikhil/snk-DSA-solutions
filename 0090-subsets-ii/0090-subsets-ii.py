class Solution(object):
    def findSets(self, idx, combSet, reqSet, nums):
        if idx >= len(nums):
            reqSet.append(tuple(combSet[:]))
            return
        
        combSet.append(nums[idx])
        self.findSets(idx+1, combSet, reqSet, nums)
        combSet.pop()
        self.findSets(idx+1, combSet, reqSet, nums)
    
    
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        idx = 0
        reqSet = []
        combSet = []
        nums.sort()
        self.findSets(idx, combSet, reqSet, nums)
        # reqSet = tuple(reqSet)
        return set(reqSet)
        
        
        
        