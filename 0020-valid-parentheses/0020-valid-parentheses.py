class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         parStack = []
        
#         for ch in s:
#             if ch == '(' or ch == '[' or ch == '{':
#                 parStack.append(ch)
#             elif ch == ')' and len(parStack) != 0:
#                 if parStack.pop() != '(':
#                     return False
#             elif ch == ']' and len(parStack) != 0:
#                 if parStack.pop() != '[':
#                     return False
#             elif ch == '}' and len(parStack) != 0:
#                 if parStack.pop() != '{':
#                     return False
#             else:
#                 return False
            
#         if len(parStack) != 0:
#             return False
        
#         return True


        parStack = []
        bracketsDict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        for ch in s:
            if ch in bracketsDict.keys():
                parStack.append(ch)
            elif len(parStack) == 0 or ch != bracketsDict[parStack.pop()]:
                return False
            
        # if len(parStack) == 0:
        #     return True
        # else:
        #     return False
        
        return len(parStack) == 0