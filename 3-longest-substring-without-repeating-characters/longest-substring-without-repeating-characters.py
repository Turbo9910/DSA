class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        seen = set()
        answer = 0
        l = 0
        for r in range(len(s)):
          
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            if s[r] not in seen:
                seen.add(s[r])
            answer = max(answer,r-l+1)
        return answer


        