

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num) - 1
        while n >= 0:
            if num[n]== '1' or num[n]=='3' or num[n]=='5' or num[n]=='7'or  num[n]=='9':
                return num[:n+1]
            
            n-=1
        return ""
       
      
       
       
         