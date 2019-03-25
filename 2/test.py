from linkedlist2 import Node, LinkedList2

n1 = Node(13)
n2 = Node(15)
n3 = Node(27)
n4 = Node(87)
n5 = Node(777)
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


print("TEST FIND")
s_list.print_all_nodes()
print("-----------")
print(s_list.find(13))
print(n2)



print("TEST FIND ALL")
s_list.print_all_nodes()
print(s_list.find_all(20))
print(n1, n4, n5)
arr_node = s_list.find_all(20)
for i in range(len(arr_node)):
    print(arr_node[i], arr_node[i].value)



print("TEST DELETE")
s_list.print_all_nodes()
s_list.delete(13, True)
print("После удаления:")
s_list.print_all_nodes()
print("Сверим концы")
print(s_list.head, s_list.tail)
#print(s_list.head.next.value, n5.value)
#print(s_list.head.value, n5.prev.value)
#print(s_list.head.prev)
node = s_list.head
while node is not None:
    print(node.prev, node, node.next)
    node = node.next



print("TEST INSERT")
n6 = Node(999)
n6.prev = n4
n6.next = n5
new = Node(10000)
s_list.insert(n5, new)
s_list.print_all_nodes()

print(s_list.head, n1)
print(s_list.head.next, n2)
print(s_list.tail, n5)
print(s_list.tail.prev, n4)

node = s_list.head
while node is not None:
    print(node.prev, node, node.next)
    node = node.next



print("TEST ADD IN HEAD")
new = Node(10000)
s_list.add_in_head(new)
s_list.print_all_nodes()
print(s_list.head, new, s_list.tail, n5)
print(new.next, n1)
print(new, n1.prev)
node = s_list.head
while node is not None:
    print(node.prev, node, node.next)
    node = node.next



print("TEST CLEAN")
s_list.print_all_nodes()
print("---------")
s_list.clean()
s_list.print_all_nodes()
print(s_list.head, s_list.tail)
node = s_list.head
while node is not None:
    print(node.prev, node, node.next)
    node = node.next


print("TEST LEN")
s_list.print_all_nodes()
print("Длина списка")
l = s_list.len()
print(l)
node = s_list.head
while node is not None:
    print(node.value)
    node = node.next

