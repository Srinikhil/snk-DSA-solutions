class Solution(object):
    
    # reqSet = []
    
    def cSum(self, idx, combSet, candidates, target, reqSet):
        
        if idx == len(candidates):
            if target == 0:
                reqSet.append(combSet[:])
            return
        
        if candidates[idx] <= target:
            combSet.append(candidates[idx])
            self.cSum(idx, combSet, candidates, target-candidates[idx], reqSet)
            combSet.pop()
            
            
        self.cSum(idx+1, combSet, candidates, target, reqSet)
        
    
    def combinationSum(self, candidates, target):
        idx = 0
        combSet = []
        combSum = 0
        reqSet = []
        self.cSum(idx, combSet, candidates, target, reqSet)
        return reqSet
        