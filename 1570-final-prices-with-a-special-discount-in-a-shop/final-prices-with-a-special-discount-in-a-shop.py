class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = list()
        p = None
        for i in range(len(prices)):
            p = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    p = prices[i] - prices[j]
                    break
            result.append(p)
        return result
        