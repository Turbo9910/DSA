class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num =int("".join(map(str, digits)))
        num = num + 1
        r = list()
        while num > 0:
            r.append(num % 10)
            num = num // 10
        return r[::-1]

        