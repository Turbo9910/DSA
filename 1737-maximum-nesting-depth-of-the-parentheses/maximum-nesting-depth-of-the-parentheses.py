class Solution:
    def maxDepth(self, s: str) -> int:
        st = list()
        max_count = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append(s[i])
            elif s[i] == ')':
                max_count = max(max_count,len(st))
                st.pop()
        return max_count



        