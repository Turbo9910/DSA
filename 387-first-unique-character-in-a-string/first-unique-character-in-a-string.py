class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_map = Counter(s)
        key = list()
        for k,v in s_map.items():
            if v == 1:
                key.append(k)
        for i,v in enumerate(s):
            if v in key:
                return i
        return -1

        