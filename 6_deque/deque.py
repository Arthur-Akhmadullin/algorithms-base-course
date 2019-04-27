class Deque:
    def __init__(self):
        self.deque = []
    # инициализация внутреннего хранилища

    def addFront(self, item):
        self.deque.insert(0, item)
    # добавление в голову

    def addTail(self, item):
        self.deque.append(item)
    # добавление в хвост

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop(0)
        # удаление из головы
        return None # если очередь пуста

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop()
        # удаление из хвоста
        return None # если очередь пуста

    def size(self):
        return len(self.deque) # размер очереди