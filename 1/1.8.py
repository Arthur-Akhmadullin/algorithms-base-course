from linkedlist import Node, LinkedList

def make_list_from_linked_list(llist):

    list = []

    node = llist.head
    while node != None:
        list.append(node.value)
        node = node.next
    return list



def sum_elem_linked_lists(link_listA, link_listB):

    sum_list = []

    len_A = link_listA.len()
    len_B = link_listB.len()

    if len_A == len_B:
        listA = make_list_from_linked_list(link_listA)
        listB = make_list_from_linked_list(link_listB)
        for i in range(len_A):
            sum_list.append(listA[i] + listB[i])
    else:
        print("Длины списков не равны")

    return sum_list


s_list_A = LinkedList()
s_list_B = LinkedList()

s_list_A.add_in_tail(Node(1))
s_list_A.add_in_tail(Node(4))
s_list_A.add_in_tail(Node(9))

s_list_B.add_in_tail(Node(3))
s_list_B.add_in_tail(Node(2))
s_list_B.add_in_tail(Node(8))

print(sum_elem_linked_lists(s_list_A, s_list_B))