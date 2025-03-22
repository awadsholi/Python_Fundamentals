class Node:   # Single Node Implementation
    def __init__(self, data):
        self.data = data  # value
        self.next = None  # pointer

    def __repr__(self):
        return f"Node {self.data}"


class LinkedList:
    def __init__(self):
        self.head = None  # Starting Point (Linked_List -> Head -> None)

    def __repr__(self):
        nodes = []   # List for representation
        current = self.head  # Start from Head to represent LinkedList

        while current:
            nodes.append(repr(current))
            current = current.next  # Move to next node

        return "->".join(nodes) + "->None"  # String representation

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to current head
        self.head = new_node  # Update head to new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Case: empty list
            self.head = new_node
            return  # Added missing return

        current = self.head
        while current.next:  # Fixed iteration to stop at last node
            current = current.next
        current.next = new_node  # Append to end

    def insert_after_node(self, selected_data, data):
        current = self.head
        while current:
            if current.data == selected_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return f"Selected data {selected_data} Not found"

    def delete(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
                return  # Added return after deleting head

        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        return f"Selected data {data} Not found"

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return f"Found Node --->{data}"
            current = current.next
        return "Node Not Found"

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.print_list()
    ll.insert_at_beginning(16)
    ll.print_list()
    ll.insert_at_end(25)
    ll.print_list()
    ll.insert_after_node(10,36)
    ll.print_list()
    ll.delete(36)
    ll.print_list()