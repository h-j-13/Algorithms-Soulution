class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # list-TimeComplexity https://wiki.python.org/moin/TimeComplexity
        
        stack = []
        for c in s:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []