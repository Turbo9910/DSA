class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        n = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        present = True
        for i in range(1,n + 1):
            st = strs[0]
            st = st[:i]
            for j in range(1,len(strs)):
                if strs[j].startswith(st):
                    present = True
                else:
                    present = False
                    break
            if present:
                if len(st) >= len(longest):
                    longest = st
        return longest

        