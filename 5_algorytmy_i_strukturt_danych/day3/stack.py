class Stack:
    def __init__(self):
        self._stack = []
    def push(self, element):
        self._stack.append(element)
    def pop(self):
        return self._stack.pop()
    def size(self):
        return len(self._stack)
    def peek(self):
        return self._stack[-1]