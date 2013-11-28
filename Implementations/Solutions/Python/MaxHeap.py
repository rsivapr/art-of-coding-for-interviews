class MaxHeap:
    def __init__(self, key):
        self.heap = [0, key]

    def parent(self, index):
        if index == 1:
            return index
        else:
            return index/2

    def insert(self, key, index=None):
        if index is None:
            index = len(self.heap)
        if index == 1:
            self.heap[1] = key
        else:
            parent_index = self.parent(index)
            if key > self.heap[parent_index]:
                self.heap.append(self.heap[parent_index])
                self.insert(key, parent_index)