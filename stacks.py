class Stack:
    def __init__(self) -> None:
        self.items = []

    @property
    def top(self):
        return self.items[-1]

    def push(self, elem):
        self.items.append(elem)
        return self.items

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (not bool(self.items))

    def __repr__(self) -> str:
        return f"{self.items}"

stack = Stack()
print("Pushing into Stack",stack.push("zaeem"))
print("Pushing into Stack",stack.push('raza'))
print("Pointer TOP ->",stack.top)
print("Popped out:", stack.pop())
print("Is Stack Empty:", stack.is_empty())
print(stack)