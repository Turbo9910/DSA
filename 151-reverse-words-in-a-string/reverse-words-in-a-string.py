class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words) - 1
        r = [i for i in range(n+1)]
        i = 0

        while n >= 0:
            r[i] = words[n]
            i+=1
            n-=1
        return ' '.join(r)

        