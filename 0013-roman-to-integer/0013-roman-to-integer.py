class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToIntDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        intNum = 0
        i = 0
        j = 1
        n = len(s)
        
        while j < n:
            if romanToIntDict[s[i]] >= romanToIntDict[s[j]]:
                intNum += romanToIntDict[s[i]]
                i += 1
                j += 1

            else:
                intNum += romanToIntDict[s[j]] - romanToIntDict[s[i]]
                i += 2
                j += 2
                
        if i < n:
            intNum += romanToIntDict[s[i]]
            
        return intNum
        
        