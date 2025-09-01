class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == len(t):
            return ""
        s = sorted(s)
        t = sorted(t)
        for i,j in zip(s,t):
            if i !=j:
                return j
        return t[len(t) -1]


        