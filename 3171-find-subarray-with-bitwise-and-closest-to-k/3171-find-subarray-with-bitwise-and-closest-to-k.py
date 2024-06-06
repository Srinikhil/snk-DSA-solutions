class Solution(object):
    def changeBitCounts(self, n, flag, countBits):
        i = 0
        while n > 0:
            if n & 1:
                countBits[i] += flag
            n = n // 2
            i += 1
    
    
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        countBits = [0 for _ in range(32)]
        ans = sys.maxint
        st = 0
        cur = nums[0]
        
        for i in range(len(nums)):
            cur = cur & nums[i]
            self.changeBitCounts(nums[i], 1, countBits)
            ans = min(ans, abs(k-cur))
            
            if cur == k:
                return 0
            
            elif cur > k:
            # As numbers needs to be added to the subarray to decrease the value of cur to bring it nearer to k
                continue
            else:
                while st<=i and cur < k:
                    # Removing element by element till i
                    self.changeBitCounts(nums[st], -1, countBits)
                    st += 1
                    
                    cur = 0
                    for j in range(32):
                        # i-st+1 is nothing but the remaining size of the sub array being considered. so if it equals to countBits[j] that mean that bit is one for all the elements of that subarray so it can be considered one in the cur and others as zero.
                        if (i-st+1) == countBits[j]:
                            cur = cur | (1<<j)
                            
                    ans = min(ans, abs(k-cur))
        
        return ans