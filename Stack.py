"""
https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=1
"""

class Stack():
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []


    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def reverse_string(stack, input_str):
        for i in range(len(input_str)):
            stack.push(input_str[i])
        
        rev_str = ""

        while not stack.is_empty():

            rev_str += stack.pop()

        return rev_str


stack = Stack()

input_str = "Hello"

print(stack.reverse_string(input_str))



myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")


print(myStack.get_stack()[::-1])

