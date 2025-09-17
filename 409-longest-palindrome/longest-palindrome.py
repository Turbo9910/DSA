class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = 0
        c_map = Counter(s)

        for v in c_map.values():
            if v % 2 == 0:
                m += v
            else:
                m += v-1
        return m + 1 if m < len(s) else m