class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        v = list()
        for i in s:
            if i in vowels:
                v.append(i)
        n = len(v) - 1
        r = [i for i in range(len(s))]
        for i in range(len(s)):
            if s[i] in vowels:
                r[i] = v[n]
                n-=1
            else:
                r[i] = s[i]
        
        return ''.join(r)



        