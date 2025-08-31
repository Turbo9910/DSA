class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        new_s = ''
        for i in range(len(s)):
            new_s = s[-i:] + s[:-i]
            if goal == new_s:
                return True
        return False

        