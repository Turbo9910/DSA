import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h_map = {}
        for i in range(len(mat)):
            h_map[i] = sum(mat[i])   
    
        r = [(v, i) for i, v in h_map.items()]
        heapq.heapify(r)
        result = [heapq.heappop(r)[1] for _ in range(min(k, len(r)))]
        return result
