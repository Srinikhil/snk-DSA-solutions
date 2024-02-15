class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Brute Force
        ansArr = []
        for i in range(len(nums)):
            ansArr.append(nums[i])
        for i in range(len(nums)):
            ansArr.append(nums[i])
            
        return ansArr
        
        