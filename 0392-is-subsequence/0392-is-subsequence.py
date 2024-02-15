class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #TC - O(n), SC - O(1)
        
#         i, j = 0, 0
#         while True:
#             # if len(s) == 0:
#             #     return True
#             if i >= len(s) or j >= len(t) :
#                 break
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
        
#         if i == len(s):
#             return True
#         else:
#             return False


        i, j = 0, 0
        for j in range(len(t)):
            # if len(s) == 0:
            #     return True
            if i < len(s) and s[i] == t[j]:
                i += 1

        
        if i == len(s):
            return True
        else:
            return False
        