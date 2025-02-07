class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if not self.front:
            self.rear = None
        return temp.data

    def front_element(self):
        if self.front:
            return self.front.data
        return "Queue is empty"

    def is_empty(self):
        return self.front is None

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.front_element())  # Output: 10
print(q.dequeue())        # Output: 10
print(q.front_element())  # Output: 20
