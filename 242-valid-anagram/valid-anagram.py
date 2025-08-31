class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if len(s) != len(t):
            return False

        for k, v in s_map.items():
            if k in t_map:
                if v == t_map[k]:
                    continue
                else:
                    return False
            else:
                return False
        return True
