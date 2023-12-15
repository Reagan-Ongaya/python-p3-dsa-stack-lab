class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.max_size is not None and len(self.items) == self.max_size

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target)
        return None
