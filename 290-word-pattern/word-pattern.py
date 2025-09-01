class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        characters = [c for c in pattern]
        s_map = {}
        t_map = {}
        if len(words) !=len(characters):
            return False


        for word,c in zip(words,characters):
            if c in s_map and  s_map[c]!= word:
                return False
            if word in t_map and t_map[word]!=c:
                return False
            s_map[c] = word
            t_map[word] = c
        return True 
        