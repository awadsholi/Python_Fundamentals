class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if not self.front :
            return None

        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed_data

    def print_queue(self):
        current = self.front
        print("Queue", end="")
        while current:
            print(f" -> {current.data}", end="")
            current = current.next



if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.print_queue()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print()
    q.print_queue()