class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() > 0:
            return self.stack[self.size() - 1]
        return None


class Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        return self.stack_1.push(item)

    def dequeue(self):
        if self.stack_2.size() > 0:
            return self.stack_2.pop()
        elif self.stack_1.size() > 0:
            while self.stack_1.size() > 0:
                self.stack_2.push(self.stack_1.pop())
            return self.stack_2.pop()
        else:
            return None

    def size(self):
        return (self.stack_1.size() + self.stack_2.size())