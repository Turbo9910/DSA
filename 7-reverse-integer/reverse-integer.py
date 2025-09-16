class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        flag = False
        if x < 0:
            flag = True
            x = -x  
        
        result = []
        
        while x != 0:
            result.append(x % 10)  
            x = x // 10            
        
        
        result_integer = int("".join(map(str, result)))
        
        if flag:
            result_integer = -result_integer
        if result_integer < -2**31 or result_integer > 2**31 - 1:
            return 0  
        
        return result_integer


        