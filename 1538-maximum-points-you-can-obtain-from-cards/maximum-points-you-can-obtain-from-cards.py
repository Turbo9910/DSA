class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_points = sum(cardPoints)
        
       
        if k == n:
            return total_points
        
        window_size = n - k
        current_sum = sum(cardPoints[:window_size])
        min_subarray_sum = current_sum
        
        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray_sum = min(min_subarray_sum, current_sum)
        
        return total_points - min_subarray_sum
