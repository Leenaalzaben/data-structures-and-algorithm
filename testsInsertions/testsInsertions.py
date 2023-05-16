from inslinkedlist.inslinkedlist import LinkedList,Node

def test_linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
test_linked_list()

def test_kth_from_end_greater_than_length():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(2) == None


def test_kth_from_end_same_length():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    assert ll.kth_from_end(2) == 1


def test_kth_from_end_not_positive_integer():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(-1) == None


def test_kth_from_end_size_1():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(1) == 1


def test_kth_from_end_happy_path():
     ll = LinkedList()
     ll.head = Node(1)
     ll.head.next = Node(2)
     ll.head.next.next = Node(3)
     ll.head.next.next.next = Node(4)
     assert ll.kth_from_end(2) == 3