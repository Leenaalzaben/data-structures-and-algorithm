import unittest
from insertions.insertionlinkedlist import LinkedList

class TestInsertions(unittest.TestCase):
    def test_append(self):
        my_list = LinkedList()
        my_list.append(10)
        my_list.append(20)
        my_list.append(30)
        
        self.assertEqual(my_list.head.value, 10)
        self.assertEqual(my_list.head.next.value, 20)
        self.assertEqual(my_list.head.next.next.value, 30)
        

if __name__ == '__main__':
    unittest.main()
