class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


tree = Tree("acuff")
tree.insert("cher")
tree.insert("madonna")
tree.insert("ziggy")
tree.insert("bono")
tree.insert("elton")
tree.insert("george")
tree.insert("paul")

tree.printTree()