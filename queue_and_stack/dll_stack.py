
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        self.storage.remove_from_head()

    def len(self):
        self.storage.__len__()
        
