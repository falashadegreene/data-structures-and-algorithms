from data_structures.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            self.buckets[index] = LinkedList()
        self.buckets[index].insert((key, value))
