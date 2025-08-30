class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = 0  
        for p in s:
            if p == '(':
                if stack > 0: 
                    result.append('(')
                stack += 1
            else: 
                stack -= 1
                if stack > 0:  
                    result.append(')')

        return ''.join(result)
