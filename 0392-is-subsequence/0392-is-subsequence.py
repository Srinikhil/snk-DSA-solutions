class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while True:
            if i >= len(s) or j >= len(t):
                break
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i == len(s):
            return True
        else:
            return False
        