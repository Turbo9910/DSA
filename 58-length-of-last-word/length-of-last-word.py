class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        n = len(words) - 1
        return len(words[n])
        