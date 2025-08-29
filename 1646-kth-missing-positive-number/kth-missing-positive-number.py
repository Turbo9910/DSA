class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = list()
        i = 0
        while len(s) < k:
            if i+1 not in arr:
                s.append(i+1)
            i+=1
        
        return s[k-1]
            