class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    head = None
    def last(self, node = None):
        if(not node):
            node = self.head
        if(not node.next):
            return node
        else:
            return self.last(node.next)

    def insert(self, obj):
        if(not self.head):
            self.head = Node(obj)  # construct a node and assign it the name given
        else:
            self.last().next = Node(obj)  # find the last node
        node = Node()
        node.data = obj
        self.head = node



people = SingleLinkedList()
people.insert("bob")



pass
