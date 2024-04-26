# ll = [1, 2, 3, 4, 5]
#
# ll.append(77)
# print(ll)
#
# while ll:
#     print(ll.pop())
#

class Stack:
    def __init__(self):
        self.internal_stack = []

    def push(self, value):
        self.internal_stack.append(value)

    def pop(self):
        return self.internal_stack.pop()

    def peek(self):
        return self.internal_stack[-1]

s2 = Stack()

s2.push(89)
s2.push(69)
print(s2.peek())
