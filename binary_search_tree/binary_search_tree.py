import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empty
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
                # otherwise recursion
            else:
                self.left.insert(value)
        # right side
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)





        # checking = True
        # current_node = self.value
        # print('current_node', current_node)
        # while checking is True:
        #     if value < current_node:
        #         current_node = self.right
        #         if current_node.value == None:
        #             print('current_node.value', current_node.value)
        #             current_node = value
        #             checking = False
        #         elif value < current_node:
        #             print('value', value)
        #             current_node.left = BinarySearchTree(value)
        #         else:
        #             current_node = current_node.right
        #     elif value > current_node.value:
        #         current_node = current_node.right
        #         print('current_node', current_node)
        #         if current_node is None:
        #             current_node = value
        #             checking = False
        #         elif value < current_node:
        #             print('current_node.value', current_node.value)
        #             current_node.value = current_node.left
        #         else:
        #             print('current_node', current_node)
        #             current_node.right = BinarySearchTree(value)





    # # Insert the given value into the tree
    # def insert(self, value):
    #     # to insert must have a tree or a root
    #     # 2 cases
    #
    #     # if value is less than the self.value go left make a new node/tree if empty, otherwise
    #     if value < self.value:
    #         self.left
    #         # new node
    #     # keep going (recursion)
    #     else:
    #         return
    #     # if great than or equal to then go right, make new tree/node is empty otherwise keep going recurison
    #     if value >= self.value:
    #         self.right
    #         # new node
    #     # recursion
    #     else:
    #         return




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return false
            # recurs
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)




        # # if target = self.value return it
        # if target == self.value:
        #     return target
        # # go left or right based on smaller or bigger
        # if self.right is not None:
        #     return self.right
        # else:
        #     return self.value
        #



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

        # # start here, easy
        # # if right exists, go right
        # if self.right is not None:
        #     return self.right
        # # otherwise return self.value
        # else:
        #     return self.value
        #


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # this works
        # stack = Stack()
        # stack.push(self)
        #
        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)


        # if self.right is not None:
        #     return self.right
        # else:
        #     return self.value
        #
        # if self.left is not None:
        #     return self.left
        # else:
        #     return self.value
        #
        # pass
        #



# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

    # DAY 2 Project -----------------------

    def in_order_print(self, node):
        # google in_order_print -- recursion?
        # UPER
        # U - UNDERSTAND
        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

        # P - PLAN
        #  a = sort(list)
        #  b = reverse(a)
        # recurse here?
        #   print(a)
        #
        #
        #
        #

        pass






    class BinarySearchTree:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queue
        # put root in the queue -- use Queue - already made
        queue = Queue(self.value)
        # while queue is not empty
        while queue:
        #   pop out the front of the queue
            queue.pop(self.value)
        #   if left
            if self.left > 0:
        #       add left to back of queue
                self.left = self.enqueue(node)
        #   if right:
            if self.right >= 0:
                self.right = self.enqueue(node)
        #       add right to back of queue







    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # hardest, use recursion
        # make a stack --- use Stack -- already made
        stack = Stack(node)
        # put root in stack
        # while stack not empty
        while stack:
        #   pop root out of stack
            stack.pop(node)
            if self.left:
        #       add left to stack
                self.left = self.push(node)
            if self.right:
        #       add right to stack
                self.right = self.push(node)






















    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


