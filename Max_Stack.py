class MaxStack:

    def __init__(self):
        self.stk = []
        self.max_stk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.max_stk:                  #if stack is empty, we will add val to it
            self.max_stk.append(val)
        elif self.max_stk[-1] > val:                # Checking if val in stack bigger than the current val
            self.max_stk.append(self.max_stk[-1])
        else:
            self.max_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.max_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.max_stk[-1]
        
