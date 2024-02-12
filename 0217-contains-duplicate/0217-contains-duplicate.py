class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using Hashmap
        storeMap = {}
        for i in nums:
            if i in storeMap:
                return True
            else:
                storeMap[i] = 1
                
        return False
        