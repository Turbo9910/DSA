class Solution:
    def frequencySort(self, s: str) -> str:
        c_map = Counter(s)
        j = 0
        r = ""
        c_map = dict(sorted(c_map.items(), key=lambda item: item[1], reverse=True))
        for k,v in c_map.items():
            r += k*v
        return r
        

                

        