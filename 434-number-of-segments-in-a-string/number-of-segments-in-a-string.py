class Solution:
    def countSegments(self, s: str) -> int:
        words = s.rsplit()
        return len(words)
        