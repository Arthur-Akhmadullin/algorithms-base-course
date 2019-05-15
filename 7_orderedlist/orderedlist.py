class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return +1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        if self.head is None:
            item = Node(value)
            self.head = item
            item.prev = None
            item.next = None

        else:
            newNode = Node(value)
            node = self.head
            previous = None
            #stop = False

            while node != None:
                if self.__ascending == True:
                    if self.compare(node.value, value) == +1:
                        break
                elif self.__ascending == False:
                    if self.compare(node.value, value) == -1:
                        break
                else:
                    previous = node
                    node = node.next

            '''
            while node != None and not stop:
                if node.value > value:
                    stop = True
                else:
                    prev = node
                    node = node.next
            '''


            newNode.next = node
            newNode.prev = previous
            previous.next = newNode


            if node.next == None:
                self.tail = newNode
            else:
                node.next.prev = newNode


            '''
            temp = Node(value)
            if previous == None:
                temp.next = self.head
                self.head = temp
            else:
                temp.next = node
                previous.next = temp
            # автоматическая вставка value
            # в нужную позицию
            '''

    def find(self, val):
        node = self.head
        stop = False
        while node != None and stop != True:
            if node.value == val:
                return node
            else:
                if node.value > val:
                    stop = True
                else:
                    node = node.next
        return None # здесь будет ваш код

    def delete(self, val):
        if self.head == None:
            return

        node = self.head

        while node is not None and node.value == val:
            self.head = self.head.next
            node = self.head
            if self.head == None:
                self.tail = None
            else:
                self.head.prev = None
            if all == False:
                return

        while node is not None:
            while node is not None and node.value != val:
                node = node.next
            if node is None:
                return
            old = node
            old.prev.next = node.next
            if node == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                old.next.prev = node.prev
            node = old.next

            if all == False:
                break

    def clean(self, asc):
        self.__ascending = asc
        pass # здесь будет ваш код
        '''
        if self.head == None:
            return
        node = self.head
        while node is not None:
            self.head = self.head.next
            node.value = None
            node.next = None
            node = self.head
            if node == None:
                self.tail = None
            else:
                self.head.prev = None
        '''

    def len(self):
        if self.head is None:
            return 0
        node = self.head
        length = 0
        while node is not None:
            node = node.next
            length = length + 1
        return length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0