class Solution:
    def makeGood(self, s: str) -> str:
        t = True
        while(t):
            i = 0
            j = 1
            t = False
            while j < len(s):
                if s[i].lower() == s[j].lower() and s[i]!=s[j]:
                    s = s[:i] + s[j+1:]
                    t = True
                i+=1
                j+=1  
        return s
       
        
        