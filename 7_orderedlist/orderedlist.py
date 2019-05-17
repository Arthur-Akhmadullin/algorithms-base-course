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
        node = self.head
        old = None

        while node != None:
            if self.__ascending == True and self.compare(node.value, value) == +1:
                break
            if self.__ascending == False and self.compare(node.value, value) == -1:
                break
            old = node
            node = node.next

        newNode = Node(value)
        if old == None:
            if self.tail == None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                #self.head.next = self.tail
                #self.tail.prev = self.head
        else:
            newNode.next = node
            newNode.prev = old
            old.next = newNode
            if node == None:
                self.tail = newNode
            else:
                node.prev = newNode


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
        return None


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
            break
            #if all == False:
                #return

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
            break

            #if all == False:
                #break

    def clean(self, asc):
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

        self.__ascending = asc


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
        try:
            if ''.join(v1.split()) < ''.join(v2.split()):
                return -1
            elif ''.join(v1.split()) == ''.join(v2.split()):
                return 0
            else:
                return +1
        except Exception:
            print("Сравниваются не строки")