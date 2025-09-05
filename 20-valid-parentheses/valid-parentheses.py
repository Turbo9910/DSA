class Solution:
    def isValid(self, s: str) -> bool:
        start = ['(','{','[']
        st = list()
        for i in s:
            if i in start:
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                s = st.pop()
                if s == '(' and i != ')':
                    return False
                if s == '{' and i !='}':
                    return False
                if s== '[' and i !=']':
                    return False
        if len(st) == 0:
            return True
        return False

        