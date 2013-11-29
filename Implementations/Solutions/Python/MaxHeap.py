def heapify(lst):
    heap = []
    for item in lst:
        heappush(heap, item)
    return heap

def heappush(heap, item, index=None):
    if index is None:
        index = len(heap)
        heap.append(0)
    if index == 0:
        heap[0] = item
    else:
        parent_index = (index-1)/2
        if item > heap[parent_index]:
            heap[index] = heap[parent_index]
            heappush(heap, item, parent_index)
        else:
            heap[index] = item
    return heap


def heappop(heap, index=0):
    child_index = (2*index + 1, 2*index + 2)
    if child_index[0] > len(heap) - 1 or child_index[1] > len(heap) - 1:

    children = {child_index[0]: heap[child_index[0]], child_index[1]: heap[child_index[1]]}

    heappop(heap, )


def head(heap):
    return heap[0]
