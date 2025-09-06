class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        seen = set()
        count = 0
        max_count = 0
        for i in range(len(s)):
            seen.clear()
            count = 0
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    count+=1
            if count > max_count:
                max_count = count
        return max_count
        