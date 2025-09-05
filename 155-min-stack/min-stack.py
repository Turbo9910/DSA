class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []   

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.arr:
            val = self.arr.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if not self.arr:
            return -1
        return self.arr[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
