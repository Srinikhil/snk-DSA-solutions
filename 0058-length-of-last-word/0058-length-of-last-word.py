class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
#         reqWord = ''
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == ' ':
#                 return reqWord
#             reqWord = s[i] + reqWord
            
#         print(reqWord)

# Approach 1
#         reqWordCount = 0
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == ' ' and reqWordCount != 0:
#                 return reqWordCount
#             elif s[i] == ' ':
#                 continue
#             else:
#                 reqWordCount += 1
                
#         return reqWordCount

# Approach using split()

        # wordBag = s.split()
        # return len(wordBag[-1])
        i = len(s) - 1
        reqWordCount = 0
        while i>=0 and s[i] == ' ':
            i -= 1
        while i>=0 and s[i] != ' ':
            reqWordCount += 1
            i -= 1
        
        return reqWordCount
    
    

