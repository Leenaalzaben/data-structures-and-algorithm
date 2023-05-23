
import pytest
from Linked_List.linked_list import Node,LinkedList

def test_zip_Lists():
    linkedlist1 = LinkedList()
    linkedlist1.insert(1)
    linkedlist1.insert(2)
    linkedlist1.insert(3)
    linkedlist1.insert(4)

    linkedlist2 = LinkedList()
    linkedlist2.insert(9)
    linkedlist2.insert(8)
    linkedlist2.insert(7)
    linkedlist2.insert(6)   