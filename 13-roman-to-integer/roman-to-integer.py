class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                if s[i:i+2] == "IV":
                    count += 4
                elif s[i:i+2] == "IX":
                    count += 9
                elif s[i:i+2] == "XL":
                    count += 40
                elif s[i:i+2] == "XC":
                    count += 90
                elif s[i:i+2] == "CD":
                    count += 400
                elif s[i:i+2] == "CM":
                    count += 900
                i += 2   # skip next char since it’s already counted
            else:
                if s[i] == 'I':
                    count += 1
                elif s[i] == 'V':
                    count += 5
                elif s[i] == 'X':
                    count += 10
                elif s[i] == 'L':
                    count += 50
                elif s[i] == 'C':
                    count += 100
                elif s[i] == 'D':
                    count += 500
                elif s[i] == 'M':
                    count += 1000
                i += 1
        return count

            
            

                

        