class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        deleted = [False for _ in range(len(s))]
        positions = [[] for _ in range(26)]
        
        for i in range(len(s)):
            if s[i] != '*':
                positions[ord(s[i]) - ord('a')].append(i)
            else:
                for j in range(26):
                    if len(positions[j]) > 0:
                        deleted[positions[j][-1]] = True
                        deleted[i] = True
                        positions[j].pop()
                        break
                    
        
        res = ""
        for i in range(len(s)):
            # if i not in deleted.keys():
                # res += s[i]
            if deleted[i] == False:
                res += s[i]
                
        # print(res)
        return res
                
