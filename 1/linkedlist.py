class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None


    def add_in_tail(self, item):

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item


    def print_all_nodes(self):

        node = self.head
        while node != None:
            print(node.value)
            node = node.next


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
            if all == False:
                return


        while node is not None:

            while node is not None and node.value != val:
                old = node
                node = node.next

            if node is None:
                return

            old.next = node.next
            node = old.next
            if old.next == None:
                self.tail = old

            if all == False:
                break

        #if old == None:
            #self.tail = old


    def clean(self):

        if self.head == None:
            return
        node = self.head
        while node is not None:
            self.head = self.head.next
            node.value = None
            node = self.head
        self.tail = None
        return


    def len(self):

        self.length = 0
        if self.head != None:
            self.length += 1
            node = self.head
            while node.next != None:
                node = node.next
                self.length += 1
        return self.length


    def insert(self, afterNode, new):

        newNode = Node(new)
        if self.head == None:
            return
        node = self.head
        while node is not None:
            if node.value == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node.next.next == None:
                    self.tail = node.next
                break
            node = node.next
        return

