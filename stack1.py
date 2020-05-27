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

