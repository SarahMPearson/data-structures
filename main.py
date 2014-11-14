from stack import *
from que import *
from recursion import *

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')

print("1st off the stack: {0}".format(food.pop()))

people = Que()

people.enqueue('Bob')
people.enqueue('Sara')
people.enqueue('Jill')

print("1st off the Queue: {0}".format(people.dequeue()))
print("2nd off the Queue: {0}".format(people.dequeue()))

print(fact(5))

print(fib(8))
print(fib(3))

for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))