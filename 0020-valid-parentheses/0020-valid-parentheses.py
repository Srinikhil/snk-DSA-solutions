class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parStack = []
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                parStack.append(ch)
            elif ch == ')' and len(parStack) != 0:
                if parStack.pop() != '(':
                    return False
            elif ch == ']' and len(parStack) != 0:
                if parStack.pop() != '[':
                    return False
            elif ch == '}' and len(parStack) != 0:
                if parStack.pop() != '{':
                    return False
            else:
                return False
            
        if len(parStack) != 0:
            return False
        
        return True