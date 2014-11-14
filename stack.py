
class Stack:
    data = []  # creating the array(stack)
    def push(self, name):   # self = food in this case
        self.data.append(name)
    def pop(self):
        return self.data.pop()

