class MaxHeap:
    def __init__(self, key):
        self.heap = [0, key]

    def parent(self, index):
        if index <= 1:
            return 1
        else:
            return index/2

    def put(self, key, index=None):
        if index is None:
            index = len(self.heap)
            self.heap.append(0)
        if index == 1:
            self.heap[1] = key
        else:
            parent_index = self.parent(index)
            if key > self.heap[parent_index]:
                self.heap[index] = self.heap[parent_index]
                self.put(key, parent_index)
            else:
                self.heap[index] = key