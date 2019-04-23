class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def rotation(self, step):
        if self.size() > 0:
            for i in range(step):
                head = self.dequeue()
                self.enqueue(head)
        else:
            print("Пустая очередь")
            return