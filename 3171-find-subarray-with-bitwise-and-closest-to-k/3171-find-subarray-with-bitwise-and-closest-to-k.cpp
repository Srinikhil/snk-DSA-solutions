class Solution {
public:
    void changeBitCounts(int n, int flag, vector<int> &countBits) {
        int i = 0;
        while (n>0) {
            if (n&1) {
                countBits[i] += flag;
            }
            n = n/2;
            i++;
        }
    }
    
    
    int minimumDifference(vector<int>& nums, int k) {
        vector <int> countBits(32, 0);
        int ans = INT_MAX;
        int st = 0;
        int cur = nums[0];
        
        for(int i=0; i<nums.size(); i++) {
            cur = cur & nums[i];
            changeBitCounts(nums[i], 1, countBits);
            ans = min(ans, abs(k-cur));
            
            if (k == cur) return 0;
            
            if (cur>k) continue;
            
            else {
                while (st<=i && cur<k) {
                    changeBitCounts(nums[st], -1, countBits);
                    st++;
                    
                    cur = 0;
                    for (int j=0; j<32; j++) {
                        if (i-st+1 == countBits[j]) {
                            cur = cur | (1<<j);
                        }
                    }
                ans = min(ans, abs(k-cur));
                }
                
            }
        }
        
    return ans;
    }
};