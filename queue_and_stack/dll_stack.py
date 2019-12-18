import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stack is last in first out
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adding to the end
    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    # removing from the end
    def pop(self):
        if self.size is not 1:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return

    def len(self):
        return self.size