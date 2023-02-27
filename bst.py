# Binary search tree

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.value)
        if self.right:
            self.right.inorderTraversal()

    def preorderTraversal(self):
        print(self.value)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()

    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.value)




bst = BinarySearchTree(5)
bst.insert(3)
bst.insert(9)
bst.insert(2)
bst.insert(4)

bst.inorderTraversal()
bst.preorderTraversal()
bst.postorderTraversal()



