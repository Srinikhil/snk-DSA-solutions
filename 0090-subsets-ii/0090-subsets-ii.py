class Solution(object):
    # Recursion using additional set
#     def findSets(self, idx, combSet, reqSet, nums):
#         if idx >= len(nums):
#             reqSet.append(tuple(combSet[:]))
#             return
        
#         combSet.append(nums[idx])
#         self.findSets(idx+1, combSet, reqSet, nums)
#         combSet.pop()
#         self.findSets(idx+1, combSet, reqSet, nums)
    
    
    
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
        
#         idx = 0
#         reqSet = []
#         combSet = []
#         nums.sort()
#         self.findSets(idx, combSet, reqSet, nums)
#         # reqSet = tuple(reqSet)
#         return set(reqSet)

    def findSets(self, idx, combSet, reqSet, nums):
        reqSet.append(combSet[:])
        
        for i in range(idx, len(nums)):
            if i>idx and nums[i] == nums[i-1]:
                continue
                
            combSet.append(nums[i])
            self.findSets(i+1, combSet, reqSet, nums)
            combSet.pop()
    
    
    
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
        
        
        return reqSet
        
        
        
        