class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keyMap = {}
        for i in s:
            if i not in keyMap:
                keyMap[i] = 1
            else:
                keyMap[i] += 1
                
        
        for i in t:
            if i not in keyMap:
                return False
            elif keyMap[i] == 1:
                del keyMap[i]
            else:
                keyMap [i] -= 1
            
        if len(keyMap) == 0:
            return True
        else:
            return False
        