class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for op in operations:
            if op == 'C':
                points.pop()
            elif op == 'D':
                points.append(2*points[len(points)- 1])
            elif op == '+':
                s = points[len(points)-1] + points[len(points) -2]
                points.append(s)
            else:
                points.append(int(op))
        return sum(points)
            
        