class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words) - 1
        r = list()

        while n >= 0:
            r.append(words[n])
            n-=1
        return ' '.join(r)

        