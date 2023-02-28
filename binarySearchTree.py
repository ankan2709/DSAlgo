class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class bst:
    def __init__(self):
        self.root = None

    # add a node to the binary search tree
    def add(self, current, value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = None(value)
                else:
                    self.add(current.left, value)
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)

