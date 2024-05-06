class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums)-1
        low = 0
        mid = high // 2
        
        while high >= low:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid-1
                mid = high // 2
            else:
                low = mid+1
                mid = ((high + low) // 2)
                
        return -1
        