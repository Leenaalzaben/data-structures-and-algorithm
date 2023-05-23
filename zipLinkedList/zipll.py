
class Node:
    """A node in a linked list."""

    def __init__(self, value, next=None):
        """
        Initialize a new node with a given value and next node.

        Args:
            value: The value to be stored in the node.
            next: The next node in the linked list.
        """
        self.value = value
        self.next = next



class LinkedList:
    """A linked list data structure."""
    def __init__(self, head=None):
        """
        Initialize a new linked list with a given head node.

        Args:
            head: The first node of the linked list.
        """
        
        self.head=head
        
    def zip_Lists(self, list1, list2):
        """
        Zips two linked lists together by alternating their elements.

        Parameters:
            list1 (LinkedList): The first linked list.
            list2 (LinkedList): The second linked list.
        """

        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2
            current2.next = next1
            last_current1 = current1.next
            current1 = next1
            current2 = next2
            if not current1 and current2:
                last_current1.next = current2

        return list1
        
        

if __name__=="__main__":
    # Create instances of ll and nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Create the first ll
    linked_list1 = LinkedList(node1)
    node1.next = node2
    node2.next = node3

    # Create the second ll
    linked_list2 = LinkedList(node4)

    # Print the zipped ll
    zipped_list = linked_list1.zip_Lists(linked_list1, linked_list2)
    current_node = zipped_list.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next
    
 
   
    


