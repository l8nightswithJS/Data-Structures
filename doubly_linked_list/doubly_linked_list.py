"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            print("Node added")
        else:
            new_node = ListNode(value, None, self.head)
            self.head.prev = new_node
            self.head = self.head.prev
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 1:
            stored_val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return stored_val
        elif self.length == 0:
            pass
        else:
            self.length -= 1
            self.head.next = None
            self.tail.prev = None
            self.head = self.head.next
            return self.head

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 1:
            stored_val = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return stored_val
        elif self.length == 0:
            pass
        else:
            self.length -= 1
            self.tail.prev = None
            self.tail.next = None
            return self.tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        stored_val = self.head
        while stored_val is not None:
            if node.value == stored_val.value:
                break
            stored_val = stored_val.next
        self.delete(stored_val)
        self.add_to_head(stored_val.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        stored_val = self.head
        while stored_val is not None:
            if node.value == stored_val.value:
                break
            stored_val = stored_val.next
        self.delete(stored_val)
        self.add_to_tail(stored_val.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            stored_val = self.head
            while stored_val is not None:
                if node.value == stored_val.value:
                    break
                stored_val = stored_val.next
            if node.value == self.head.value:
                if self.length == 2:
                    self.head = self.tail
                else:
                    self.head = node.next
            if node.value == self.tail.value:
                self.tail = node.prev
            if stored_val.next is not None:
                stored_val.next.prev = node.prev
            if stored_val.prev is not None:
                stored_val.prev.next = node.next
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        stored_val = self.head
        while stored_val is not None:
            if stored_val.value > max_value:
                max_value = stored_val.value
            stored_val = stored_val.next
        return max_value