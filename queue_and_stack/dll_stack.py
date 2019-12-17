import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()


    def push(self, value):
        self.size += 1
        while len(self.storage) != 0:
            self.storage.add_to_head(value)
            self.storage.pop()

    def pop(self):
        pass

    def len(self):
        return self.size
