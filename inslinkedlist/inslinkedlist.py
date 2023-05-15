class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def insertBefore(self, value, newValue):
        if self.head is None:
            return

        if self.head.value == value:
            new_node = Node(newValue)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.next.value == value:
                break
            n = n.next

        if n.next is None:
            return

        new_node = Node(newValue)
        new_node.next = n.next
        n.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.value == value:
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next


