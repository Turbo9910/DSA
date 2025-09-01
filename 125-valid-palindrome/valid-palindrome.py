class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                r = r + i.lower()
            else:
                continue
              
        print(r)
        if r[::-1] == r:
            return True
        else:
            return False

        