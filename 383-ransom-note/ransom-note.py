class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0 or len(magazine) == 0:
            return False
        if len(ransomNote) == 0 and len(magazine) == 0:
            return True
        c_map = {}
        for i in magazine:
            if i in c_map:
                c_map[i]+=1
            else:
                c_map[i] = 1
        for i in ransomNote:
            if i not in c_map or c_map[i] == 0:
                return False
            c_map[i]-=1
        return True
        
        