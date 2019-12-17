import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # print('self.size')
        # print(self.size)
        # Why is our DLL(DOUBLE LINKED LIST) a good choice to store our elements? -->
        self.storage = DoublyLinkedList()
        print('self.storage')
        print(self.storage)


    def enqueue(self, value):
        # self.storage.insert(0, value)
        # self.size.storage = self.storage.len()
        self.size += 1
        # return?
        self.storage.add_to_head(value)

# DELETE
    def dequeue(self):
        self.size - 1
        node = storage.
        self.storage.delete(node)
        # print('self.storage.pop()')
        # print(self.storage.pop())
        # return self.storage.pop()

    def len(self):
        self.storage.get_max()
        # print('len(self.storage)')
        # print(len(self.storage))
        # return len(self.storage)
