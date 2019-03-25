class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None


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


    def clean(self):
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


    def len(self):
        if self.head is None:
            return 0
        node = self.head
        length = 0
        while node is not None:
            node = node.next
            length = length + 1
        return length



    def insert(self, afterNode, newNode):
        if afterNode == None and (self.head is None or self.head is not None):
            self.add_in_tail(newNode)
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                newNode.prev = node
                if node.next == None:
                    self.tail = newNode
                else:
                    node.next.prev = newNode
                node.next = newNode
                #if node.next.next == None:
                    #self.tail = node.next
                break
            node = node.next
        return


    def add_in_head(self, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            self.head = self.head.prev