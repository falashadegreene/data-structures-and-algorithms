from data_structures.invalid_operation_error import InvalidOperationError
class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_rear = Node(value)
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            old_rear = self.rear
            self.rear = new_rear
            old_rear.next = new_rear

    def dequeue(self):

        if self.is_empty():
            raise InvalidOperationError("Method does not work on empty queue")

        old_front = self.front
        self.front = self.front.next
        return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError("InvalidOperationError")
        return self.front.value

    def is_empty(self):
        return self.front is None

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
