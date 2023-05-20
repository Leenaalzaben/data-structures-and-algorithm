class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
  

class linked_list:
    def __init__(self): 
        self.head = None

    def __insert_single(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def __get_kth_from_end(k, current_node):
        if current_node == None:
            return ((None, -1))
        value, index = linked_list.__get_kth_from_end(k, current_node.next)
        if index + 1 == k:
            return (current_node.data, index + 1)
        return ((value, index + 1)) 

    def insert(self, data):
        if hasattr(data, '__len__'):
            for element in data:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node
        else:
            self.__insert_single(data)

    def includes(self, value):
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node != None):
            if current_node.next == None:
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_before(self, value, data):
        current_node = self.head
        past_node =  None

        if self.head == None:
            raise Exception(f"Value {value} was not found")
        
        if self.head.data == value:
            self.insert(data)
            return
        
        while current_node != None:
            if current_node.data == value:
                temp = self.head
                self.head = current_node
                self.insert(data)
                past_node.next = self.head
                self.head = temp
                print(self)
                return
            past_node = current_node
            current_node = current_node.next 
        raise Exception(f"Value {value} was not found")
         
    def insert_after(self, value, data):
        if self.head == None:
            raise Exception(f"Value {value} was not found")

        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                temp = self.head
                self.head = current_node.next
                self.insert(data)
                current_node.next = self.head
                self.head = temp
                print(self)
                return
    
            current_node = current_node.next
        raise Exception(f"Value {value} was not found")
    
    def kthFromEnd(self, k):
        value ,index = linked_list.__get_kth_from_end(k, self.head)
        if value == None or k<0:
            raise Exception(f"K index is bigger than Linked list size by {k - index}")
        return value

    def __str__(self):
        result = ""

        current_node = self.head
        while current_node != None:
            result += f"{{ {current_node.data} }} -> "
            current_node = current_node.next
        result += "NULL"

        return result
   
