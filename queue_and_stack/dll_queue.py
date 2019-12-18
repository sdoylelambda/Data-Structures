import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

# DELETE
    def dequeue(self):
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None


    def len(self):
        return self.size
