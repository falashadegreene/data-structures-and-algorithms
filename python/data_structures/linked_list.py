class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        text = ""
        current = self.head

        while current is not None:
            text += "{" + str(current.value) + "} => "
            current = current.next
        return text + "null"

    def includes(self, target):
        # method body here
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

    class Node:
        def __init__(self, value):
            self.value = value

    class TargetError:
        pass
