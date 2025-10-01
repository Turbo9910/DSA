class Solution:
    def frequencySort(self, s: str) -> str:
        c_map = Counter(s)
        j = 0
        r = [0] * len(s)
        c_map = dict(sorted(c_map.items(), key=lambda item: item[1], reverse=True))
        for k,v in c_map.items():
            while c_map[k] != 0:
                r[j] = k
                c_map[k] -=1
                j +=1
        r = "".join(map(str, r))
        return r
        

                

        