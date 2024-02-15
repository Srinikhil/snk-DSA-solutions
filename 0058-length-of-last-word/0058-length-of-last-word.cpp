class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = s.size();
        int i = size - 1;
        int reqWordCount = 0;
        
        while (i>=0 && s[i] == ' ') {
                i--;
        }
        
        while (i>=0 && s[i] != ' ') {
            reqWordCount += 1;
            i--;
        }
        
        return reqWordCount;
        
    }
};