class Solution(object):
    def findUniqComb(self, idx, combSet, reqSet, candidates, target):
        if target == 0:
            reqSet.append(combSet[:])
            return
        
        for i in range(idx, len(candidates)):
            
            # condition to check duplicate by checking prev one in the sorted array
            if (i > idx) and (candidates[i] == candidates[i-1]):
                continue
            
            if candidates[i] > target:
                break
            
            combSet.append(candidates[i])
            self.findUniqComb(i+1, combSet, reqSet, candidates, target-candidates[i])
            combSet.pop()
            
    
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        idx = 0
        reqSet = []
        combSet = []
        candidates.sort()
        self.findUniqComb(idx, combSet, reqSet, candidates, target)
        return reqSet