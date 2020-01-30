import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        if self.value > value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if greater go to right child
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
        # if not child, on that side, insert else try again starting from the child on appropriate
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # Find
    # look at root, if root is it return
    # if value is less than node, go left and repeat
    # if no left child, return none
    # if value is >= node, go right and repeat. if not right child return none
    # and then something... maybe 3 statements in while loop
    # variables? at least 2
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)











    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # use stack
    def in_order_print(self, node):
        # make a stack
        stack = Stack()
        # add root to stack
        stack.push(node)
        # while there is stuff in the stack
        if stack is not None:
        # pop 13 and save in temp
            temp = stack.pop()
        # DO THE THING!!!!
        # if temp.left add to stack
            if temp.left:
                return self.left.in_order_print(node)
        # if temp.right add to stack
            if temp.left:
                return self.right.in_order_print(node)





















    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # use queue
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # use stack
    def dft_print(self, node):
        pass









































    # STRETCH Goals -------------------------

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

    def delete_node(self, node):
        pass