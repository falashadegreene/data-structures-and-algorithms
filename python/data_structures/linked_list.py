class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None

    def __str__(self):
        text = ""
        current = self.head

        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            print(text)
            current = current.next
        return text + "NULL"

    def includes(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):

        new_node = Node(value)

        current = self.head

        while current:
            if not current.next:

                current.next = new_node

                break
            else:
                # moves to the next one
                current = current.next

    def insert_before(self, search_value, value):
        node_two = Node(value)
        if not self.head:
            raise TargetError

        if self.head.value == search_value:
            self.insert(value)
            return

        # start at head or beginning
        current = self.head

        while current and current.next:
            if current.next.value == search_value:

                node_two.next = current.next

                current.next = node_two

                break
            # Danger

            else:
                current = current.next
        else:
            raise TargetError

    def insert_after(self, search_value, value):

        current = self.head

        while current:
            if current.value == search_value:
                self.insert_before(current.next.value, value)
                return
            else:
                current = current.next
        raise TargetError


def kth_from_end(self, k):

        n = 0
        curr = self.head

        while curr:
            curr = curr.next
            n = n + 1
        loop_count = n - k
        if k >= n:
            raise TargetError
        elif k < 0:
            raise TargetError

        curr = self.head
        for i in range(loop_count):
            if i == loop_count - 1:
                return curr.value
            curr = curr.next
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class TargetError(Exception):
    pass

