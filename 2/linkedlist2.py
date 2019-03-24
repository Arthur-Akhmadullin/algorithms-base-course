class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        array_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                array_nodes.append(node)
            node = node.next
        return(array_nodes)


    def delete(self, val, all=False):
        if self.head == None:
            return

        node = self.head
        old = None

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
            #if old.next == None:
                #self.tail = old

            if all == False:
                break

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

    def add_in_head(self, newNode):
        pass # здесь будет ваш код