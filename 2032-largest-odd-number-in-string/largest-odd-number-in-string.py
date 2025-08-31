

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num) - 1
        odd = ['1','3','5','7','9']
        while n >= 0:
            if num[n] in odd:
                return num
            num = num[:-1]
            n-=1
        return ""
       
      
       
       
        