class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i, j = 0, n-1
        
        while i < j:
            if lower(s[i]).isalnum() and lower(s[j]).isalnum():
                if lower(s[i]) != lower(s[j]):
                    return False
                else:
                    i += 1
                    j -= 1
                    
            elif lower(s[i]).isalnum() != True:
                i += 1
            elif lower(s[j]).isalnum() != True:
                j -= 1
                
        return True