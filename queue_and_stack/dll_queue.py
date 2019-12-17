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
        return self.storage.add_to_tail(value)

# DELETE
    def dequeue(self):
        if self.size >= 1:
            self.size -= 1
            self.storage.remove_from_head()
        else:
            return
        # print('self.storage.pop()')
        # print(self.storage.pop())
        # return self.storage.pop()

    def len(self):
        return self.size
        # return self.storage.get_max()
        # print('len(self.storage)')
        # print(len(self.storage))
        # return len(self.storage)
