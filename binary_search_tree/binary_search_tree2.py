

#

class BinarySearchTree2:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        # compare root now
        if self.value > value:
            if not self.left:
                self.left = BinarySearchTree2(value)
            else:
                # if something already there recurse
                self.left.insert(value)

        else: # value is >= Node
            # do same but right child
            if not self.right:
                self.left = BinarySearchTree2(value)
            else:
                self.right.insert(value)





















    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # easy
    # just go right
    def get_max(self):
        # recursive solution
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # iterative solution
        max_value = self.value
            # create a reference to the current node and update it
            # as we traverse the tree
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
                # move pointer to next right
            current = current.right

        return max_value

        # traverse tree -recursive depth traversal keep going right --
        # hard
    def for_each(self, cb):
         # recursive solution
        # call the callback, don't forget
        cb(self.value)
        # recurse
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)



        # iterative approach using stack - depth first traversal
        # make a stack
        # start at root -pop-(avoid infinite loop)  put in temp variable put in stack
        # while stack is not empty:
        # DO THE THING ---
        # look left - if something add it to stack
        # look right - if something add it to the stack
        # repeat until no left then look right if right add it
        # pop it -- when sees nothing - and save in temp

        # notes from Brian
        # make a stack
        # add root to stack
        # while there is stuff in the stack
        # pop 13 and save in temp
        # DO THE THING!!!!
        # if temp.left add to stack
        # if temp.right add to stack








        # breadth first traversal --- use Queue instead of stack -- first in first out -- back of the line
        # recursion does not work
        # 1 level of tree at a time hitting all nodes then going down
        # look left and right
        # look left and right of both children
        #


  # notes from Brian
        # make a queue
        # add root to stack
        # while there is stuff in the queue
        # pop 13 and save in temp
        # DO THE THING!!!!
        # if temp.left add to queue
        # if temp.right add to queue