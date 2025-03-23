class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        popped = self.top.data
        self.top = self.top.next

    def top_value(self):
        return self.top.data

    def print_stack(self):
        current = self.top
        while current:
            print(f"-> {current.data}")
            current = current.next









if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.print_stack()
    s.pop()
    print()
    print()
    s.print_stack()