class MinStack:

    def __init__(self):
        self.Stack = []
        self.TrackerStack = []
        
    def push(self, value: int) -> None:
        self.Stack.append(value)

        if len(self.TrackerStack) >= 1:
            self.TrackerStack.append(min(value, self.TrackerStack[-1]))
        else:
            self.TrackerStack.append(value)

    def pop(self) -> None:
        self.Stack.pop()
        self.TrackerStack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.TrackerStack[-1]
        