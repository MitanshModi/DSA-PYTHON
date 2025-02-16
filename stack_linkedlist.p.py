class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # Output: 20
print(s.pop())   # Output: 20
print(s.size())  # Output: 1
