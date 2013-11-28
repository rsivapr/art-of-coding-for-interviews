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

    The running time of this is now O(N*k) which is much
    smaller that O(N*logN) under the assumption that k<<N.
    '''
    smalls = origin[:k]
    for number in origin:
        if max(smalls) > number:
            smalls[smalls.index(max(smalls))] = number
    return smalls

def find_minimum(k, origin):
    '''
    Implement a Max-Heap
    '''