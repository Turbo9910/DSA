class MyStack:

    def __init__(self):
        self.arr = []
        

    def push(self, x: int) -> None:
        self.arr.append(x)

        

    def pop(self) -> int:
         a = self.arr.pop()
         return a
        

    def top(self) -> int:
        return self.arr[len(self.arr) -1]
        

    def empty(self) -> bool:
        if not self.arr:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()