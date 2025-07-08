class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in '([{':
                st.append(char)
            elif char == ')':
                if not st or st.pop() != '(':
                    return False
            elif char == ']':
                if not st or st.pop() != '[':
                    return False
            elif char == '}':
                if not st or st.pop() != '{':
                    return False
        return len(st) == 0
