class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        c = True
        i = 0
        while c:
            i = 0
            temp = s
            while i < len(temp):
                if s[i] == 'z':
                    next_ch = 'a'
                else:
                    next_ch = chr(ord(s[i]) + 1)
                s = s + next_ch
                i+=1
            if len(s) >= k:
                c = False
        return s[k-1]




        