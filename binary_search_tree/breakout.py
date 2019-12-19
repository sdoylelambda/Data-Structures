
import unittest
import sys

import io
from binary_search_tree import BinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree(5)

    def test_insert(self):
        self.bst.insert(2)

    def test_print_traversals(self):
        # WARNING:  Tests are for Print()
        # Debug calls to Print() in functions will cause failure

        stdout_ = sys.stdout  # Keep previous value
        sys.stdout = io.StringIO()

        self.bst = BinarySearchTree(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        self.bst.in_order_print(self.bst)

        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")

        sys.stdout = stdout_  # Restore stdout


if __name__ == '__main__':
    unittest.main()




# # find middle item of list
#
# # UPER
#
# # U - Understand
#
# # 1 for each item to find length of list, then / 2
# # 2 loops second 2x where the second ends, will be answer
#
# class LinkList:
#     def __init__(self):
#         self.length = 0
#         self.head = None
#
#     def insert(self, value):
#         self.length += 1
#         if self.head is None:
#             self.head = {'value': value}
#         else:
#             self.head = {'value': value, 'tail': self.head}
#
#
#     def remove(self):
#         if self.head is None:
#             return None
#         else:
#             self.length -= 1
#             value = self.head['value']
#             if self.length == 0:
#                 self.head = None
#             else:
#                self.head = self.head['tail']
#
#             return value
#
#     def reverse(self):
#         temp_head = LinkList()
#         for n in self.length:
#             temp_head.insert(self.remove())
#         self.head = temp_head.head
#
#
# test_list = LinkList()
# for item in [1,2,3]:
#     test_list.insert(item)
#
# print(test_list.remove())
# print(test_list.remove())
# print(test_list.remove())
#
#
# # reverse in linklist





