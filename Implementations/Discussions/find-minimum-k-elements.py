""" 
Question :: In an integer array with N elements (N is large),
find the minimum k elements (k<<N).

Given: A large array, say `origin`. 
"""


def find_minimum_sort(k, origin):
    '''
    Runs in O(N*log(N) time due to sorting)
    When N is large, this is not efficient.
    
    There is the additional space of O(N) taken as well.
    '''
    sorted_large = sorted(origin)
    return sorted_large[:k]

def find_minimum_pick(k, origin):
    '''
    Here, the space is O(k) instead of O(N). Definitely an
    improvement.

    The running time of this is now O(N*k) which is a better solution 
    than O(N*logN) under the assumption that k<<N.
    '''
    smalls = origin[:k]
    for number in origin:
        if max(smalls) > number:
            smalls[smalls.index(max(smalls))] = number
    return smalls

def find_minimum(k, origin):
    '''
    Implement a k-element Max-Heap.
    Space is still O(k), but the time now decreases to O(N*logk).
    Since O(1) to just look at the root of the heap (`heap.peek()`)
    Pushing an element in the heap takes O(logk) in the worst case.


    Note: Why not use Min-Heap and heapify the `origin` array? 
    Because we are able to further reduce space from O(N) to O(k).
    '''
    for number in origin:
        if number < heap.peek():
            heap.pop()
            heap.push(number)

def fin_minimum_optimized(k, origin):
    '''
    We build a Min-Heap from original array in place using Floyd's algorithm.
    Heapify takes O(N) time. 
    For the second part, where we repeatedly pop the heap, we do this in 
    O(logN) time each. So O(k*LogN).
    Can O(N) + O(k*logN) be O(N)?
    Yes. If k<O(N/logN).

    This also takes no extra space!


    '''
    minheap = heapify_floyd(origin)
    mink = []
    for i in range(k):
        new = minheap.pophead()
        mink.append(new)


