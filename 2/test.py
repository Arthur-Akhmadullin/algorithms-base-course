from linkedlist2 import Node, LinkedList2

n1 = Node(13)
n2 = Node(14)
n3 = Node(15)
n4 = Node(16)
n5 = Node(13)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

s_list = LinkedList2()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(n3)
s_list.add_in_tail(n4)
s_list.add_in_tail(n5)
'''
s_list.print_all_nodes()

arr_node = s_list.find_all(12)
for i in range(len(arr_node)):
    print(arr_node[i], arr_node[i].value)

print("--------")
s_list.delete(13, True)
s_list.print_all_nodes()
print(n1.next.value)
print(n3.next.value)
print(s_list.head, s_list.tail)
print(n1,n4)

print("--------")
n6 = Node(99)
s_list.insert(None, n6)
s_list.print_all_nodes()
print(s_list.head, n6, s_list.tail)

print(n5, n6.prev)
print(n5.next, n6)
print(n6, n4.prev)
print(n6.next, n4)

print("--------")
s_list.print_all_nodes()
n6 = Node(99)
s_list.add_in_head(n6)
print("----------")
s_list.print_all_nodes()
print(s_list.head, n6, s_list.tail, n5)
print(n6.next, n1)
print(n6, n1.prev)

s_list.print_all_nodes()
print("--------")
s_list.clean()
s_list.print_all_nodes()
print(s_list.head, s_list.tail)
node = s_list.head
while node is not None:
    print(node, node.value)
'''
s_list.print_all_nodes()
print("--------")
print(s_list.len())
