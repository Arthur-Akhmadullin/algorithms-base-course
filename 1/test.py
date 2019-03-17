from linkedlist import Node, LinkedList


def test_find_all():
    print("------TEST FIND ALL------")
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(130))
    s_list.print_all_nodes()
    try:
        if s_list.find_all(55) == [55,55]:
            print("test for value success")
        else:
            print("test for value failed")
    except Exception:
        print("error test find all")
    try:
        if s_list.find_all(1000) == []:
            print("test for None success")
        else:
            print("test for None failed")
    except Exception:
        print("error test find all")
test_find_all()


def test_delete():
    print("------TEST DELETE------")
    s_list = LinkedList()
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))

    s_list2 = LinkedList()
    s_list2.add_in_tail(Node(12))
    s_list2.add_in_tail(Node(55))
    s_list2.add_in_tail(Node(128))

    s_list3 = LinkedList()
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(12))
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(128))
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(130))
    s_list3.add_in_tail(Node(55))
    s_list3.add_in_tail(Node(55))

    s_list4 = LinkedList()

    s_list5 = LinkedList()
    s_list5.add_in_tail(Node(55))

    s_list6 = LinkedList()
    s_list6.add_in_tail(Node(12))
    s_list6.add_in_tail(Node(55))


    print("------DELETE ALONE IN BEGIN (duplicates)------")
    s_list.print_all_nodes()
    print("---------------")
    try:
        s_list.delete(55, False)
        s_list.print_all_nodes()
        if s_list.find_all(55) == [55,55] and s_list.head.value == 55 and s_list.tail.value == 128:
            print("test for alone in begin success")
        else:
            print("test for alone in begin failed")
    except Exception:
        print("error test delete")

    print("------DELETE ALONE IN MIDDLE------")
    s_list2.print_all_nodes()
    print("---------------")
    try:
        s_list2.delete(55, False)
        s_list2.print_all_nodes()
        if s_list2.find_all(55) == [] and s_list2.head.value == 12 and s_list2.tail.value == 128:
            print("test for alone in middle success")
        else:
            print("test for alone in middle failed")
    except Exception:
        print("error test delete")

    print("------DELETE ALL------")
    s_list3.print_all_nodes()
    print("---------------")
    try:
        s_list3.delete(55, True)
        s_list3.print_all_nodes()
        if s_list3.find_all(55) == [] \
                and s_list3.head.value == 12 and s_list3.tail.value == 130:

            print("test for all, flag=True success")
        else:
            print("test for all, flag=True failed")
    except Exception:
        print("error test delete")

    print("------DELETE FROM EMPTY------")
    s_list4.print_all_nodes()
    print("---------------")
    try:
        s_list4.delete(55, True)
        s_list4.print_all_nodes()
        if s_list4.find_all(55) == [] and s_list4.head == None and s_list4.tail == None:
            print("test for empty, flag=True success")
        else:
            print("test for empty, flag=True failed")
    except Exception:
        print("error test delete")

    print("------DELETE FROM LIST WITH ONE NODE------")
    s_list5.print_all_nodes()
    print("---------------")
    try:
        s_list5.delete(55, True)
        s_list5.print_all_nodes()
        if s_list5.find_all(55) == [] and s_list5.head == None and s_list5.tail == None:
            print("test for flag=True success")
        else:
            print("test for flag=True failed")
    except Exception:
        print("error test delete")

    print("------DELETE FROM TWO------")
    s_list6.print_all_nodes()
    print("---------------")
    try:
        s_list6.delete(55, True)
        s_list6.print_all_nodes()
        if s_list6.find_all(55) == [] and s_list6.head.value == 12 and s_list6.tail.value == 12:
            print("test for two, flag=True success")
        else:
            print("test for two, flag=True failed")
    except Exception:
        print("error test delete")
test_delete()


def test_clean():
    print("------TEST CLEAN------")
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(130))
    s_list.print_all_nodes()
    print("---------------")
    try:
        s_list.clean()
        s_list.print_all_nodes()
        if s_list.head == None and s_list.tail == None:
            print("test for clean success")
        else:
            print("test for clean failed")
    except Exception:
        print("error test clean")
test_clean()


def test_length():
    print("------TEST LENGTH------")
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(130))
    s_list.print_all_nodes()
    try:
        print(s_list.len())
        if s_list.len() == 5:
            print("test length success")
        else:
            print("test lenght failed")
    except Exception:
        print("error test lenght")
test_length()


def test_insert():
    print("------TEST INSERT------")
    s_list = LinkedList()
    s_list.add_in_tail(Node(12))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(55))
    s_list.add_in_tail(Node(130))
    s_list.print_all_nodes()
    print("---------------")
    try:
        s_list.insert(128, 1001)
        s_list.print_all_nodes()
        node = s_list.head
        count = 0
        while node != None:
            if node.value == 128 and node.next.value == 1001:
                count = count + 1
            if node.value == 1001 and node.next.value == 55:
                count = count + 1
            node = node.next
        if count == 2:
            print("test insert success")
        else:
            print("test insert failed")
    except Exception:
        print("error test insert")
test_insert()